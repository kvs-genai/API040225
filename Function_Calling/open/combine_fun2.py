import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

tools = [
    {
        "type" : "function",
        "function" : {
            "name" : "get_weather",
            "description" : "Get current temperatures for a given location",
            "parameters" : {
                "type" : "object",
                "properties" : {
                    "location" : {
                        "type" : "string",
                        "description" : "City and country e.g. Bogota, Columbia"
                    }
                },
                "required" : ["location"],
                "additionalProperties" : False
            }
        },
        "strict" : True
    },
    {
        "type" : "function",
        "function" : {
            "name" : "send_email",
            "description" : "Send an email to a given recipient with a subject and message",
            "parameters" : {
                "type" : "object",
                "properties" : {
                    "to" : {
                        "type" : "string",
                        "description" : "Recipient email address",
                    },
                    "subject" : {
                        "type" : "string",
                        "description" : "email subject line"
                    },
                    "body" : {
                        "type" : "string",
                        "description" : "body of the email messsage"
                    }
                },
                "required" : ["to", "subject", "body"],
                "additionalProperties" : False
            }
        },
        "strict" : True
    }
]

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role" : "user", "content" : "Can you send an email to ilan@example.com and katia@example.com saying hi?"}],
    tools=tools
)

def get_weather_details(**args):
    print("get weather details function called")
    print(args)

def send_email(**args):
    print("Send email function called")
    print(args)

def call_function(name, args):
    if name == "get_weather":
        return get_weather_details(**args)
    if name == "send_email":
        return send_email(**args)
    

if completion.choices[0].message.tool_calls:
    for tool_call in completion.choices[0].message.tool_calls:
        name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)

        result = call_function(name, args)
else:
    print("Error in generating response")