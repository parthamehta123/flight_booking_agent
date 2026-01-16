# app/agent/nodes/llm_planner.py

import json
import os
from typing import Optional, Dict

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


SYSTEM_PROMPT = """
You are a flight booking assistant.

Extract structured fields from user input and return ONLY valid JSON.

Fields:
- origin (3-letter airport code, uppercase)
- destination (3-letter airport code, uppercase)
- date (ISO format: YYYY-MM-DD)
- passengers (integer)

If a field is missing, omit it.

Example:
User: "book flight from sfo to jfk tomorrow for 2 people"
Response:
{
  "origin": "SFO",
  "destination": "JFK",
  "date": "2026-01-17",
  "passengers": 2
}
"""


def llm_extract_slots(text: str) -> Optional[Dict]:
    """
    Uses an OpenAI-compatible API to extract structured slots.
    Returns dict on success, None on failure.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or OpenAI is None:
        return None

    try:
        client = OpenAI(api_key=api_key)

        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": text},
            ],
            temperature=0,
        )

        content = resp.choices[0].message.content
        parsed = json.loads(content)

        if isinstance(parsed, dict):
            return parsed

    except Exception:
        return None

    return None
