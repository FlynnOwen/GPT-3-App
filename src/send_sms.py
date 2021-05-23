"""
Send a text / message using Twilio
"""
import os
from twilio.rest import Client


# Set API variables
ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

# Authenticate client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Send message
message = client.messages.create(
                     body="Back rub please?",
                     from_='+15012328789',
                     to='+64277860534'
)

# Print outputs
print(message.error_code)

