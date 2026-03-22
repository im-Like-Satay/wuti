import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from until.prompt import SYSTEM_MESSAGE as sm

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def callAi(inputData):
    client = genai.Client(api_key=GEMINI_API_KEY)

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        config=types.GenerateContentConfig(temperature=0.1, system_instruction=sm),
        contents=inputData,
    )
    print(response.text)
