from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message.content
