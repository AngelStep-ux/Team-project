import psycopg2
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST

def connect_to_db():
    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
        return conn
    except Exception as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None


def create_tables(conn):
    cursor = conn.cursor()
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id SERIAL PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                profile_url TEXT,
                age INTEGER,
                sex INTEGER,
                city TEXT
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS favorites (
                favorite_id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(user_id),
                added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS photos (
                photo_id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(user_id),
                photo_url TEXT,
                likes_count INTEGER
            );
        ''')

        conn.commit()
    except Exception as e:
        print(f"Ошибка создания таблиц: {e}")
    finally:
        cursor.close()
