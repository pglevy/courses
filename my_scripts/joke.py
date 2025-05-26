from dotenv import load_dotenv
import os
from anthropic import Anthropic

# Load environment variables from .env file
load_dotenv()

client = Anthropic()

my_joke = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    messages=[{"role": "user", "content": "Tell me a joke about cats."}]
)

print(my_joke.content[0].text)