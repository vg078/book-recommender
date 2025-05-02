import os
import textwrap
from openai import OpenAI
from dotenv import load_dotenv

client = OpenAI()
last_id = None
load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

def get_response(prompt):
    prompt_file = "book-recommender.txt"
    
    global last_id
    
    with open(prompt_file, "r", encoding="utf-8") as f:
        instructions = f.read()

    if last_id:
        response = client.responses.create(model="gpt-4.1", instructions=instructions,input=prompt,previous_response_id = last_id)
    else:
        response = client.responses.create(model="gpt-4.1", instructions=instructions,input=prompt)

    last_id = response.id
    return response.output_text

def chat():
    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ("exit","q","quit"):
            break

        ai_response = get_response(user_input)

        wrapped_text = textwrap.fill(ai_response, width=150)
        print("AI:", wrapped_text)
        if "Let me find you books of your interest" in wrapped_text:
            break
        else:
            last_ai_response = ai_response
    return last_ai_response

if __name__ == "__main__":
  chat()