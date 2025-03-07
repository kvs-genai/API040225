import os
from dotenv import load_dotenv
import google.generativeai as genai


#from google import genai
# client = genai.Client(os.getenv(api_key="GEMINI_API_KEY"))

# response = client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents=["Write 100 words about AI?"])

# print(response.text)



genai.configure(api_key="AIzaSyBNc8IRd0G1ri3x3yM4ThYm0Cy2Ani0K6U")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)