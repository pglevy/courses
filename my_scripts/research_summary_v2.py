from anthropic import Anthropic
from dotenv import load_dotenv
import base64
import mimetypes

load_dotenv()

client = Anthropic()

def create_image_message(image_path):
    # Open the image file in "read binary" mode
    with open(image_path, "rb") as image_file:
        # Read the contents of the image as a bytes object
        binary_data = image_file.read()
    
    # Encode the binary data using Base64 encoding
    base64_encoded_data = base64.b64encode(binary_data)
    
    # Decode base64_encoded_data from bytes to a string
    base64_string = base64_encoded_data.decode('utf-8')
    
    # Get the MIME type of the image based on its file extension
    mime_type, _ = mimetypes.guess_type(image_path)
    
    # Create the image block
    image_block = {
        "type": "image",
        "source": {
            "type": "base64",
            "media_type": mime_type,
            "data": base64_string
        }
    }
    
    return image_block

research_paper_pages = [
    "anthropic_api_fundamentals/images/research_paper/page1.png",
    "anthropic_api_fundamentals/images/research_paper/page2.png",
    "anthropic_api_fundamentals/images/research_paper/page3.png",
    "anthropic_api_fundamentals/images/research_paper/page4.png",
    "anthropic_api_fundamentals/images/research_paper/page5.png"
]

messages = [
    {
        "role": "user",
        "content": [
            *[create_image_message(page) for page in research_paper_pages],
            {"type": "text", "text": "You are a talented research assistant. Please transcribe each page of this research paper and provide a 1-2 paragraph summary of the entire paper. Be sure to include any key findings, methodologies, and conclusions. Before providing the complete summary in <summary> tags, think about each page in <thinking> tags."}
        ]
    }
]

# Streaming version
with client.messages.stream(
    model="claude-sonnet-4-20250514",
    max_tokens=2048,
    messages=messages
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)