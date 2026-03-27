import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASS'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT')
)
cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    name TEXT,
    file_id INT)

"""
)

def kitoblar():
    sql = "SELECT name, file_id FROM books ORDER BY id"
    cur.execute(sql)
    return cur.fetchall()

def saveBook(name, file_id):
    sql = "INSERT INTO books(name, file_id) VALUES (%s, %s)"
    cur.execute(sql,(name, file_id))
    conn.commit()