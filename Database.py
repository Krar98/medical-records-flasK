import sqlite3

def init_db():
    conn = sqlite3.connect('blood_bank.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS donors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            blood_type TEXT NOT NULL,
            last_donation DATE
        )
    ''')
    
    conn.commit()
    conn.close()

def insert_donor(name, blood_type):
    conn = sqlite3.connect('blood_bank.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO donors (name, blood_type) VALUES (?, ?)', (name, blood_type))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    insert_donor('محمد أحمد', 'O+')
    insert_donor('فاطمة علي', 'A-')
    print("✅ تم إعداد قاعدة البيانات بنجاح!")
