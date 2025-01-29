import sqlite3

def create_database():
    conn = sqlite3.connect('dating_bot.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        name TEXT,
        age INTEGER,
        interests TEXT
    )
    ''')
    
    conn.commit()
    conn.close()

create_database()