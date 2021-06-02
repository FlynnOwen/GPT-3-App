import random
import os
import time

from flask import Flask, request
from pymessenger.bot import Bot

import database.db_test_scripts as db

app = Flask(__name__)
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')
bot = Bot(ACCESS_TOKEN)


# We will receive messages that Facebook sends our bot at this endpoint
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    print(os.getcwd())
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

                    # Save in database
                    db.add_message(rec_message, member_id, rec_timestamp, 'received')

                    if rec_message:
                        response_sent_text = _get_message()
                        _send_message(member_id, response_sent_text)

                    # If user sends us a GIF, photo,video, or any other non-text item
                    if message['message'].get('attachments'):
                        _send_message(member_id, "My brain is not yet big enough to deal with images!")

    return "Message Processed"


def _verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")

    return 'Invalid verification token'


def _get_message():
    sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]

    return random.choice(sample_responses)


def _send_message(member_id, response):
    sent_timestamp = int(time.time() * 1000)

    # Save in database
    db.add_message(response, member_id, sent_timestamp, 'sent')

    bot.send_text_message(member_id, response)

    return "success"


if __name__ == "__main__":
    app.run()
