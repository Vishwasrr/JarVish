import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError("Set GEMINI_API_KEY in your .env file before running JarVish.")

client = genai.Client(api_key=GEMINI_API_KEY)

SYSTEM_PROMPT = """
You are JarVish.
A brutally practical execution assistant.
You help with:
- software testing
- FIX protocol
- kubernetes
- debugging
- execution planning
- routines
- productivity
- learning

Always:
- reduce ambiguity
- give actionable next steps
- avoid motivational fluff
- optimize execution speed
"""


def ask_agent(user_input):
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=user_input,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
        ),
    )

    return response.text
