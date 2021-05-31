import random
import os

from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
VERIFY_TOKEN = os.getenv('TESTINGTOKEN')
bot = Bot(ACCESS_TOKEN)


# We will receive messages that Facebook sends our bot at this endpoint
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    # Get verify token to ensure requests are legitimate
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)

    # Post request from user when a message is received
    else:

        # Get the message request
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):

                    # Cache Sender Id
                    recipient_id = message['sender']['id']

                    # Cache message received
                    rec_message = message['message'].get('text')

                    if rec_message:
                        response_sent_text = get_message()
                        send_message(recipient_id, response_sent_text)

                    # If user sends us a GIF, photo,video, or any other non-text item
                    if message['message'].get('attachments'):
                        send_message(recipient_id, "My brain is not yet big enough to deal with images!")

    return "Message Processed"


def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")

    return 'Invalid verification token'


def get_message():
    sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]

    return random.choice(sample_responses)


def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)

    return "success"


if __name__ == "__main__":
    app.run()
