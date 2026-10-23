import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

# Initializes the client (automatically picks up GEMINI_API_KEY from environment)
client = genai.Client()

MODEL = os.environ.get("LLM_MODEL", "gemini-2.5-flash")

response = client.models.generate_content(
    model=MODEL,
    contents="What is a neural network in one sentence?",
    config=types.GenerateContentConfig(
        max_output_tokens=256,
    ),
)

print(response.text)
