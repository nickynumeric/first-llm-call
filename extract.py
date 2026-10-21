import json
from dotenv import load_dotenv
from google import genai
from google.genai import types

MODEL = "gemini-3.5-flash-lite"
INSTRUCTION = 'Extract the details. Reply with JSON only, using exactly these keys: "name" (string), "city" (string), "score" (integer).'
CONFIG = types.GenerateContentConfig(
    system_instruction=INSTRUCTION,
    response_mime_type="application/json",
)

load_dotenv()
client = genai.Client()

text = "yesterday kofi (accra) managed 67 out of 100"

response = client.models.generate_content(
    model=MODEL,
    contents=text,
    config=CONFIG,
)

data = json.loads(response.text)
print(data)
print(data["name"], data["score"] + 1)
