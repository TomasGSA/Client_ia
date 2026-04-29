from env import API_OPENAI
from openai import OpenAI

client = API_OPENAI

response = client.responses.create(
  model="gpt-5.4-mini",
  input="write a haiku about ai",
  store=True,
)

print(response.output_text);