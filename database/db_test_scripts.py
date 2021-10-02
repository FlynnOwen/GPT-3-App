#! /usr/bin/env python3
import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.environ['DATABASE_URL']


def add_message(message, member_id, timestamp, direction, conversation_start):

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    cur = conn.cursor()
    try:
        cur.execute("""INSERT INTO messages 
                       (message, member_id, timestamp, direction, conversation_start) 
                       VALUES 
                       (%s, %s, %s, %s, %s)""",
                    (message, member_id, timestamp, direction, conversation_start))

        return 'Message added successfully'

    except:
        'Message could not be added'

    conn.commit()
    conn.close()


def add_user(member_id):
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    cur = conn.cursor()
    try:
        cur.execute("""INSERT INTO users 
                       (member_id) 
                       VALUES 
                       (%s)""",
                    (member_id,))

        return 'User added successfully'

    except psycopg2.errors.UniqueViolation:
        return 'This user is already in the database'

    conn.commit()
    conn.close()


def most_recent_message_timestamp(member_id):
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    cur = conn.cursor()
    try:
        cur.execute("""SELECT max(timestamp) FROM messages WHERE 
                       member_id = %s
                       """,
                    (member_id,))

    except:
        'An error has occurred'

    recent_date = cur.fetchone()
    conn.commit()
    conn.close()

    return recent_date[0]


def get_current_conversation(member_id):
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    cur = conn.cursor()
    try:
        cur.execute("""SELECT message FROM messages WHERE 
                       (member_id = %s) and (timestamp >= 
                       (SELECT MAX(timestamp) FROM messages WHERE conversation_start = 1))
                       """,
                    (member_id,))
    except:
        'An error in get_current_conversation has occurred'

    rows = cur.fetchall()
    conn.commit()
    conn.close()

    unprocessed_conversation = ['\nHuman: ' + rows[i][0] if i % 2 == 0 else '\nAI: ' + rows[i][0] for i in range(len(rows))]
    processed_conversation = ''.join(unprocessed_conversation)

    return processed_conversation
