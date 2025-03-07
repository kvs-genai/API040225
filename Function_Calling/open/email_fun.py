import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


tools = [
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
                        "description" : "Recipient email address"
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
    messages=[{"role" : "user", "content" : "Can you send an email to a@a.com and b@b.com saying hi!"}],
    tools=tools
)

print(completion.choices[0].message.tool_calls[0].function.arguments)
