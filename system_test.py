from dotenv import load_dotenv
from google import genai
from google.genai import types

MODEL = "gemini-3.5-flash-lite"
INSTRUCTION = "You are a pirate who explains everything in one sentence."
CONFIG = types.GenerateContentConfig(
		system_instruction = INSTRUCTION
		)
CONTENTS = "What is a list?"
load_dotenv()

client = genai.Client()

response = client.models.generate_content(
		model = MODEL,
		contents = CONTENTS,
		config = CONFIG,
	)

print(response.text)
