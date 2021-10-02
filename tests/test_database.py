import os

import psycopg2
from dotenv import load_dotenv

from database.db_test_scripts import add_message, add_user, most_recent_message_timestamp, get_current_conversation

load_dotenv()
DATABASE_URL = os.environ['DATABASE_URL']


def test_db_connection():
    psycopg2.connect(DATABASE_URL, sslmode='require')


def test_add_current_user():
    assert add_user('124') == 'This user is already in the database'


def test_add_new_user():
    user_id = '123'
    assert add_user(user_id) == 'User added successfully'


def test_add_message():
    message = 'Test'
    member_id = '124'
    timestamp = '1633215843337'
    direction = 'sent'
    conversation_start = 0

    assert add_message(message, member_id, timestamp, direction, conversation_start) == 'Message added successfully'


def test_most_recent_message_timestamp():
    member_id = '124'
    timestamp = '1633176546582'

    assert most_recent_message_timestamp(member_id) == timestamp


def test_get_current_conversation():
    member_id = '124'

    assert get_current_conversation(member_id) == '\nHuman: Test'
