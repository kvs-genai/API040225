import os
from dotenv import load_dotenv
from openai import OpenAI
import json
import requests

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
                "properties" : {"location" : {"type" : "string", "description" : "City and country e.g. Bogota, Columbia"}},
                "required" : ["location"],
                "additionalProperties" : False
            }
        },
        "strict" : True
    }
]

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role" : "user", "content" : "What is the weather in Hyderabad?"}],
    tools=tools
)

#print(completion.choices[0].message.tool_calls)

# ---------- 

OPEN_WEATHER_KEY = "81972bbd46f64f1e76367f7a17ee6836"

# print(completion.choices[0].message.tool_calls[0].function.name)
# print(completion.choices[0].message.tool_calls[0].function.arguments)

location = json.loads(completion.choices[0].message.tool_calls[0].function.arguments)["location"]

#print(location)

# Get webpage data using requests.get method
result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPEN_WEATHER_KEY}")

# print(result.text)
# Now pass this result to ChatGPT for weather summary

completion2 = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [
        {
            "role" : "system",
            "content" : "Act as weather analyst. I will give you the details of location and weather"
        },
        {
            "role" : "user",
            "content" : f"Location: {location} \n Weather: {result.text}"
        }
    ]
)

print(completion2.choices[0].message.content)



