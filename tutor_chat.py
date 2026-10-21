from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
MODEL = "gemini-3.5-flash-lite"
INSTRUCTION = "You are a patient Python tutor. Keep answers short and end with one practice question."
CONFIG = types.GenerateContentConfig(
		system_instruction=INSTRUCTION
		)
client = genai.Client()
history = []

while True:
    question = input("YOU: ").lower()
    if question == "quit":
        break
    history.append({"role":"user",
		"parts":[{"text":question}]
		})


    response = client.models.generate_content(
		model=MODEL,
		contents=history,
		config=CONFIG,
		)
    answer = response.text
    history.append({"role":"model",
		"parts":[{"text":answer}]
		})

    print(f"AI: {answer}")
