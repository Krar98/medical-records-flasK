from flask import Flask, render_template
from database import init_db
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecretkey'

init_db()  # تهيئة قاعدة البيانات عند التشغيل

@app.route('/')
def index():
    conn = sqlite3.connect('blood_bank.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM donors')
    donors = cursor.fetchall()
    conn.close()
    return render_template('index.html', donors=donors)

if __name__ == "__main__":
    app.run(debug=True)
