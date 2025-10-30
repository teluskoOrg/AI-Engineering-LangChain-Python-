from ollama import Client

client = Client(host='http://localhost:11434')

response = client.chat(
    model='mistral',
    messages=[
        {'role': 'user', 'content': 'name a bollywood comedy movie with srk, just the name'}
    ]
)

print(response)


# Step To Run PGM

# Step-1:   uv add ollama
# Step-2:   python ollamasdk.py 