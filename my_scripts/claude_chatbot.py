from dotenv import load_dotenv
from anthropic import AsyncAnthropic
import asyncio

#load environment variable
load_dotenv()

#automatically looks for an "ANTHROPIC_API_KEY" environment variable
client = AsyncAnthropic()

model="claude-3-haiku-20240307"
max_tokens=1000

conversation = []

async def streaming_chat(user_input):
    global conversation
    conversation.append({"role": "user", "content": user_input})
    
    async with client.messages.stream(
        model=model,
        max_tokens=max_tokens,
        messages=conversation
    ) as stream:
        async for text in stream.text_stream:
            print(text, end='', flush=True)
            print()  # Print a newline after the streaming response
    final_message = await stream.get_final_message()
    conversation.append({"role": "assistant", "content": final_message.content})

while True:
    if not conversation:
        print("What's on your mind? Type 'exit' to end the chat.")
    
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chat ended.")
        break

    asyncio.run(streaming_chat(user_input))