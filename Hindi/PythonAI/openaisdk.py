from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input="name a bollywood comedy movie with srk, just the name"
)

print(response.output_text)