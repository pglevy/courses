from dotenv import load_dotenv
from anthropic import Anthropic

#load environment variable
load_dotenv()

#automatically looks for an "ANTHROPIC_API_KEY" environment variable
client = Anthropic()

model="claude-3-haiku-20240307"
max_tokens=1000

def generate_questions(topic, num_questions):
    """
    Generates a list of questions based on the given topic using the Anthropic API.
    
    :param topic: The topic for which to generate questions.
    :param num_questions: The number of questions to generate.
    :return: A list of generated questions.
    """
    prompt = f"Generate some questions about {topic}. Begin each question with a number, starting with 1."
    
    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system="You are an expert in theoretical physics and your purpose is to generate thought-provoking questions for classroom discussions.",
        temperature=0.7,
        messages=[{"role": "user", "content": prompt}],
        stop_sequences=[str(num_questions+1)]  # Stop after generating the specified number of questions,
    )
    
    questions = response.content[0].text.strip().split('\n')
    print("Generated Questions:")
    for question in questions:
        print(question)
    print ("Stop Reason:", response.stop_reason, response.stop_sequence) # Print the reason for stopping the generation

generate_questions("Hawking radiation", 3)