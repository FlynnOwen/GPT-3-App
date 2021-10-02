import os

import pytest
import psycopg2
from dotenv import load_dotenv

from database.db_test_scripts import add_message, add_user, most_recent_message_timestamp, get_current_conversation

load_dotenv()
DATABASE_URL = os.environ['DATABASE_URL']


def test_db_connection():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    cur = conn.cursor()

    # Use a list here to insert query parameters into the query string.
    cur.execute(
        """
        SELECT * 
        FROM messages
        """
    )

    result = cur.fetchone()

    print(result)

    cur.close()
