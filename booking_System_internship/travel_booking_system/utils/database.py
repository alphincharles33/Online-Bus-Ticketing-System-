# database.py
import sqlite3

def create_transaction_table():
    conn = sqlite3.connect('transactions1.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS transactions12 (
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT,
                destination TEXT,
                quantity varchar,
                price REAL,
                timestamp TEXT
                )""")
    conn.commit()
    conn.close()

def insert_transaction(source, destination, quantity, total_price):
    conn = sqlite3.connect('transactions1.db')
    c = conn.cursor()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO transactions12 (source, destination, quantity, price, timestamp) VALUES (?, ?, ?, ?, ?)",
               (source, destination, quantity, total_price, timestamp))
    conn.commit()
    conn.close()
