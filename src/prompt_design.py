input_prompt = input("Type message you would like to send: ")

default_prompt = """The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.

Human: Hello, who are you?
AI: I am an AI created by OpenAI. How can I help you today?"""

full_prompt = default_prompt + "\nHuman: " + input_prompt + "\n"

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

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
print(response)
print(response_text)

print(full_prompt)

print(full_prompt + response_text)

second_prompt = full_prompt + response_text

second_input_prompt = input()
second_full_prompt = second_prompt + "\nHuman: " + second_input_prompt + "\n"

response = openai.Completion.create(
  engine="davinci",
  prompt=second_full_prompt,
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=["\n", " Human:", " AI:"]
)

response_text = response.get('choices')[0].get('text')
print(response_text)

print(second_full_prompt + response_text)