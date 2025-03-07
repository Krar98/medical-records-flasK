# medical-records-flasK
Blood bank

from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from database import init_db, insert_match, insert_incoming, insert_outgoing, get_records

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/match', methods=['GET', 'POST'])
def match():
    if request.method == 'POST':
        data = request.form
        insert_match(data)
        flash('تمت إضافة السجل بنجاح!', 'success')
        return redirect(url_for('match'))

    records = get_records('match_records')
    return render_template('match_record.html', records=records)

@app.route('/incoming', methods=['GET', 'POST'])
def incoming():
    if request.method == 'POST':
        data = request.form
        insert_incoming(data)
        flash('تمت إضافة السجل بنجاح!', 'success')
        return redirect(url_for('incoming'))

    records = get_records('incoming_records')
    return render_template('incoming_record.html', records=records)

@app.route('/outgoing', methods=['GET', 'POST'])
def outgoing():
    if request.method == 'POST':
        data = request.form
        insert_outgoing(data)
        flash('تمت إضافة السجل بنجاح!', 'success')
        return redirect(url_for('outgoing'))

    records = get_records('outgoing_records')
    return render_template('outgoing_record.html', records=records)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
