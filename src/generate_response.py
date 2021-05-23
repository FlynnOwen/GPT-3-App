"""
Generate a response from the OpenAI API
"""

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = input('Input a prompt to send to the bot: ')

response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=25)

response_text = response.get('choices')[0].get('text')

print(response_text)