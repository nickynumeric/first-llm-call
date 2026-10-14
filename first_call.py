import time
from dotenv import load_dotenv
from google import genai
from google.genai import errors

MODEL = "gemini-3.5-flash-lite"
load_dotenv()
client = genai.Client()

for attempt in range(1,4):
    try:
        response = client.models.generate_content(
		model = MODEL,
		contents = "Explain what a variable is in one sentence.",
		)
        print(response.text)
        break
    except errors.ServerError as e:
        print(f"Attempt {attempt} failed: {e.code}")
        time.sleep(5 * attempt)
