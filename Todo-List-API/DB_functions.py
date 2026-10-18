import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


DB_NAME = os.getenv('DB_NAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')


conn = psycopg2.connect(dbname=DB_NAME, password=DB_PASSWORD, user='postgres')
cur = conn.cursor()

# add new user to DB
def add_user(data: dict, token):
    insert_query = """
    INSERT INTO users (name, email, password, token)
    VALUES (%s, %s, %s, %s);
    """

    values = list(data.values())
    values.append(token)
    print(values)
    cur.execute(insert_query, tuple(values))
    conn.commit()


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

# check if email exists in DB
def email_exists(email: str) -> bool:
    cur.execute("""
        SELECT exists (SELECT 1 FROM users WHERE email = %s);
    """, (email,))

    return  cur.fetchall()[0][0]