import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [
        {
            "role" : "user",
            "content" : [
                {
                    "type" : "text",
                    "text" : "what is this image?"
                },
                {
                    "type" : "image_url",
                    "image_url" : {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
                    }
                },
            ],
        }
    ],
)

print(response.choices[0].message)
