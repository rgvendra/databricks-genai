import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY automatically

message = client.messages.create(
    model="claude-opus-5",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "This is my Hello World claude code..."}
    ],
)

for block in message.content:
    if block.type == "text":
        print(block.text)
