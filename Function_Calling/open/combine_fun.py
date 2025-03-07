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
    model="gpt-4o-mini",
    messages=[{"role" : "user", "content" : "Send an email to a@a.com saying hi"}],
    tools=tools
)

tool_call = completion.choices[0].message.tool_calls[0]

args = json.loads(tool_call.function.arguments)

print(args)
