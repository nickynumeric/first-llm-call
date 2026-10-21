import time
from dotenv import load_dotenv
from google import genai
from google.genai import errors

MODEL = "gemini-3.5-flash-lite"
load_dotenv()
client = genai.Client()
history = []

while True:
    question = input("You: ").lower()
    if question == "quit":
        break
    history.append({"role":"user", "parts":[{"text":question}]})
    for attempt in range(1,4):
        try:
            response = client.models.generate_content(
		model = MODEL,
		contents = history,
		)
            answer = response.text
            print(f"AI: {answer}")
            history.append({"role":"model", "parts":[{"text":answer}]})
            break
        except errors.ServerError as e:
            print(f"Attempt {attempt} failed: {e.code}")
            time.sleep(5 * attempt)
