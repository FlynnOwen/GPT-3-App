#! /usr/bin/env python3
import os
import openai
from dotenv import load_dotenv

from database.db_test_scripts import get_current_conversation

load_dotenv()

DEFAULT_PROMPT = """The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.

Human: Hello, who are you?
AI: I am an AI created by OpenAI. How can I help you today?"""


def gen_response(input_prompt, conversation_start, member_id):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    print(conversation_start)
    if conversation_start == 1:
        full_prompt = DEFAULT_PROMPT + "\nHuman: " + input_prompt + "\nAI:"

    else:
        full_conversation = get_current_conversation(member_id)
        print(full_conversation)
        full_prompt = DEFAULT_PROMPT + full_conversation + "\nAI:"

    response = openai.Completion.create(
      engine="davinci",
      prompt=full_prompt,
      temperature=0.9,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.6,
      stop=["\n", " Human:", " AI:"]
    )

    response_text = response.get('choices')[0].get('text')

    return response_text
