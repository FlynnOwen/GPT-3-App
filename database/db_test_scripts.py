import sqlite3
import os

def add_message(message, member_id, timestamp, direction):
    print(os.getcwd())
    conn = sqlite3.connect("../database/API-App-DB.db")
    cur = conn.cursor()

    cur.execute("""INSERT INTO messages 
                   (message, member_id, timestamp, direction) 
                   VALUES 
                   (?, ?, ?, ?)""",
                (message, member_id, timestamp, direction))

    conn.commit()
    conn.close()


def add_user(number, name):
    conn = sqlite3.connect('API-App-DB.db')
    cur = conn.cursor()

    cur.execute("""INSERT INTO users 
                   (member_id, name) 
                   VALUES 
                   (?,?)""",
                (number, name))

    conn.commit()
    conn.close()
