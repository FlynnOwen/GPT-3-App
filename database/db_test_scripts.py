import sqlite3

from src.prompt_design import DEFAULT_PROMPT


def add_message(message, member_id, timestamp, direction):
    if direction == 'sent':
        conversation_start = 0
    else:
        conversation_start = 1

    conn = sqlite3.connect("../database/API-App-DB.db")
    cur = conn.cursor()

    cur.execute("""INSERT INTO messages 
                   (message, member_id, timestamp, direction, conversation_start) 
                   VALUES 
                   (?, ?, ?, ?, ?)""",
                (message, member_id, timestamp, direction, conversation_start))

    conn.commit()
    conn.close()


def add_user(member_id):
    conn = sqlite3.connect('../database/API-App-DB.db')
    cur = conn.cursor()
    try:
        cur.execute("""INSERT INTO users 
                       (member_id) 
                       VALUES 
                       (?)""",
                    (member_id,))
    except:
        'This user is already in the database'

    conn.commit()
    conn.close()


def user_most_recent_message(member_id):
    conn = sqlite3.connect('../database/API-App-DB.db')
    cur = conn.cursor()
    try:
        cur.execute("""SELECT max(timestamp) FROM users WHERE 
                       (member_id) = (?)
                       """,
                    (member_id,))
    except:
        'An error has occurred'

    conn.commit()
    conn.close()


def get_current_conversation(member_id):
    conn = sqlite3.connect('../database/API-App-DB.db')
    cur = conn.cursor()
    try:
        cur.execute("""SELECT message FROM messages WHERE 
                       (member_id = ?) and (timestamp >= 
                       (SELECT MAX(timestamp) FROM messages WHERE conversation_start = 1))
                       """,
                    (member_id,))
    except:
        'An error in get_current_conversation has occurred'

    rows = cur.fetchall()
    conn.commit()
    conn.close()

    unprocessed_convo = ['\nHuman: ' + rows[i][0] if i % 2 == 0 else '\nAI: ' + rows[i][0] for i in range(len(rows))]
    processed_convo = ''.join(unprocessed_convo)

    full_convo = DEFAULT_PROMPT + processed_convo

    return full_convo
