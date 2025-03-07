import os
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


functions = [
    {
        "name" : "handle_greeting",
        "description" : "respond to user greeting",
        "parameters" : {"type" : "object", "properties" : {"greeting" : {"type" : "string"}}}
    },
    {
        "name" : "handle_feedback",
        "description" : "handle user's feedback",
        "parameters" : {"type" : "object", "properties" : {"feedback" : {"type" : "string"}}}
    },
    {
        "name" : "reply_to_question",
        "description" : "Reply to a question",
        "parameters" : {"type" : "object", "properties" : {"question" : {"type" : "string"}}}
    },
    {
        "name" : "handle_contextual_query",
        "description" : "handle contextual queries based on previous conversations",
        "parameters" : {"type" : "object", "properties" : {"query" : {"type" : "string"}}}
    },
    {
        "name" : "handle_irrelevant_input",
        "description" : "handle irrelevant or unrecognized input",
        "parameters" : {"type" : "object", "properties" : {"input" : {"type" : "string"}}}
    }
]

def handle_greetings(**args):
    print("User is greeting")

def chat_with_function_call(user_input):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages=[{"role" : "system", "content" : "You are a food delivery agent customer support. Answer all queries related to food only"},{"role" : "user", "content" : user_input}],
        functions = functions,
        function_call="auto"
    )

    function_call = response.choices[0].message.function_call

    args = json.loads(function_call.arguments)
    name = function_call.name

    print(args)
    print(name)

    if name == "handle_greeting":
        return handle_greetings(**args)


while True:
    user_input = input("User: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Goodbye")
        break

    chat_with_function_call(user_input)