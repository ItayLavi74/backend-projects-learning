import psycopg2
import os

DB_NAME = os.getenv('DB_NAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')

conn = psycopg2.connect(dbname=DB_NAME, password=DB_PASSWORD, user='postgres')
cur = conn.cursor()


# creates the DB table in postgresSQL if not exists
def create_DB_if_not_exists():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            name VARCHAR(255), 
            email VARCHAR(255) PRIMARY KEY,
            password VARCHAR(255), 
            token VARCHAR(255)
        );
        """)
    conn.commit()


def is_new_email(email):
    cur.execute(f"""
        SELECT exists (SELECT 1 FROM users WHERE email = {email});
    """)
    print(cur.fetchall())
