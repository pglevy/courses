from dotenv import load_dotenv
from anthropic import Anthropic

#load environment variable
load_dotenv()

#automatically looks for an "ANTHROPIC_API_KEY" environment variable
client = Anthropic()

max_tokens=1000

def compare_model_capabilities():
    models = ["claude-3-5-haiku-latest", "claude-3-7-sonnet-latest", "claude-sonnet-4-20250514"]
    task = """
    Generate a login form in HTML using the UK.gov design system.
    The form should include fields for username, password, and a submit button.
    Ensure the form is accessible and follows best practices for web development.
    """

    for model in models:
        answers = []
        response = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": task}]
        )
        answers.append(response.content[0].text)
            
        print(f"Model: {model}")
        print(f"Answers: ", answers)

compare_model_capabilities()