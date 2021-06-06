import os
import openai

DEFAULT_PROMPT = """The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.

Human: Hello, who are you?
AI: I am an AI created by OpenAI. How can I help you today?"""

def gen_response(input_prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    full_prompt = DEFAULT_PROMPT + "\nHuman: " + input_prompt + "\nAI:"

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

'''
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
'''