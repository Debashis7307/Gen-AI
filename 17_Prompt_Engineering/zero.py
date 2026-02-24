# Zero Shot Prompting
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Zero Shot Prompting: Directly giving the inst to the model
SYSTEM_PROMPT = "You should only and only ans the coding related questions. Do not ans anything else. Your name is Aarav. If user asks something other than coding, just say sorry its not my domain. and what ever u ans should be short and crisp."

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": "what is polymorphism in OOP?" }
    ]
)

print(response.choices[0].message.content)
# 1. Zero-shot Prompting: The model is given a direct question or task without prior examples.