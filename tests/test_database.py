import os

import pytest
import psycopg2
from dotenv import load_dotenv

from database.db_test_scripts import add_message, add_user, most_recent_message_timestamp, get_current_conversation

load_dotenv()
DATABASE_URL = os.environ['DATABASE_URL']


def test_db_connection():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')


def test_add_current_user():
    assert add_user('4918590254824555') == 'This user is already in the database'


def test_add_new_user():
    user_id = '123'
    assert add_user(user_id) == 'User added successfully'

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    cur = conn.cursor()
    
    cur.execute("""DELETE FROM users 
                       WHERE
                       member_id =
                       (%s)""",
                (user_id,))

    cur.close()



