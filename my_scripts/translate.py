from dotenv import load_dotenv
from anthropic import Anthropic

#load environment variable
load_dotenv()

#automatically looks for an "ANTHROPIC_API_KEY" environment variable
client = Anthropic()

def translate_text(text, language):
    """
    Translates the given text into the specified language using Anthropic's API.
    
    :param text: The text to translate.
    :param language: The target language for translation.
    :return: The translated text.
    """
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        messages=[
            {"role": "user", "content": f"Translate the following text into {language}: {text}. Respond with the content of `text` only."}
        ]
    )
    
    print(response.content[0].text.strip()) 

translate_text("kitten", "Portuguese")