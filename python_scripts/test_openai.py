from openai import OpenAI

# Create client
client = OpenAI(api_key="secrets.yaml")  # <- Replace with your real key

# Create a simple chat completion
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! Can you confirm this works?"}
    ]
)

print(response.choices[0].message.content)
