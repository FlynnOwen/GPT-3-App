import sqlite3


def add_message(message, number, datetime, direction):
    conn = sqlite3.connect('API-App-DB.db')
    cur = conn.cursor()

    cur.execute("""INSERT INTO messages 
                   (message, number, datetime, direction) 
                   VALUES 
                   (?, ?, ?, ?)""",
                (message, number, datetime, direction))

    conn.commit()
    conn.close()


def add_user(number, name):
    conn = sqlite3.connect('API-App-DB.db')
    cur = conn.cursor()

    cur.execute("""INSERT INTO users 
                   (number, name) 
                   VALUES 
                   (?,?)""",
                (number, name))

    conn.commit()
    conn.close()
