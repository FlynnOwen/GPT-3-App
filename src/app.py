#! /usr/bin/env python3
import os
import time

from flask import Flask, request
from pymessenger.bot import Bot

import database.db_test_scripts as db
from prompt_design import gen_response

app = Flask(__name__)
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')
bot = Bot(ACCESS_TOKEN)


# We will receive messages that Facebook sends our bot at this endpoint
@app.route("/", methods=['GET', 'POST'])
def receive_message():

    # Get verify token to ensure requests are legitimate
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return _verify_fb_token(token_sent)

    # Post request from user when a message is received
    else:

        # Get the message request
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):

                    # Cache metadata and payload
                    member_id = message['sender']['id']
                    rec_message = message['message'].get('text')
                    rec_timestamp = message['timestamp']

                    # Determine if this is the start of a new conversation
                    conversation_start = _get_recent_conversation(member_id)

                    # Save rec in database
                    db.add_message(rec_message, member_id, rec_timestamp, 'received', conversation_start)

                    # Add user to database
                    db.add_user(member_id)

                    if rec_message:
                        response_sent_text = _get_message(rec_message, conversation_start, member_id)
                        _send_message(member_id, response_sent_text, conversation_start)

                    # If user sends us a GIF, photo,video, or any other non-text item
                    if message['message'].get('attachments'):
                        _send_message(member_id, "My brain is not yet big enough to deal with images!")

    return "Message Processed"
    #return request.base_url

def _get_recent_conversation(member_id):
    recent_msg_timestamp = db.most_recent_message_timestamp(member_id)
    current_time = int(time.time() * 1000)
    try:
        time_difference = current_time - int(recent_msg_timestamp)
    except TypeError:
        time_difference = 300001

    if time_difference <= 300000:
        conversation_start = 0

    else:
        conversation_start = 1

    return conversation_start


def _verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")

    return 'Invalid verification token'


def _get_message(rec_message, conversation_start, member_id):
    response_text = gen_response(rec_message, conversation_start, member_id)

    return response_text


def _send_message(member_id, response, conversation_start):
    sent_timestamp = int(time.time() * 1000)

    bot.send_text_message(member_id, response)

    # Save sent message in database
    db.add_message(response, member_id, sent_timestamp, 'sent', 0)

    return "success"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
