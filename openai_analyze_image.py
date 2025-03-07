import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role":"user",
            "content":[
                {
                    "type":"text",
                    "text":"what is this image?"
                },
                {
                    "type":"image_url",
                    "image_url":
                    {
                        "url":"https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
                    } 
                }
             ]

        }
    ]
)

print(completion.choices[0].message.content)