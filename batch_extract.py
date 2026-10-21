import json
import pandas as pd
from dotenv import load_dotenv
from google import genai
from google.genai import types

MODEL = "gemini-3.5-flash-lite"
INSTRUCTION = "Extract the details. Reply with JSON only, using exactly these keys: 'name' (string), 'city' (string), 'score' (integer). If a detail is not in the text, use null for it. Never guess."
CONFIG = types.GenerateContentConfig(
    system_instruction=INSTRUCTION,
    response_mime_type="application/json",
)

load_dotenv()
client = genai.Client()

texts = [
    "Ama from Takoradi got eighty-two points on the test.",
    "yesterday kofi (accra) managed 67 out of 100",
    "Esi, Kumasi, scored 91",
    "the weather is nice today",
]

rows = []
failed = []
columns = ["name", "city", "score"]

for text in texts:
    try:
        response = client.models.generate_content(
            model=MODEL, contents=text, config=CONFIG
        )
        data = json.loads(response.text)

        if None in data.values():
            raise ValueError(f"missing value {data}")

        rows.append(data)
    except Exception as e:
        failed.append({"text": text, "error": str(e)})

df = pd.DataFrame(rows)
print(df)
print(f"Failed: {len(failed)}")
print(failed)
df.to_csv("extracted.csv", index=False)
