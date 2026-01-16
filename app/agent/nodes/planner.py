import re
import dateparser
from datetime import datetime, timedelta


def extract_slots(text: str, state: dict):
    text_lower = text.lower()

    # --- Airports ---
    match = re.search(r"from ([a-z]{3})", text_lower)
    if match:
        state["origin"] = match.group(1).upper()

    match = re.search(r"to ([a-z]{3})", text_lower)
    if match:
        state["destination"] = match.group(1).upper()

    # --- Passengers ---
    match = re.search(r"(\d+) people", text_lower)
    if match:
        state["passengers"] = int(match.group(1))

    # --- Dates (robust handling) ---
    today = datetime.now().date()

    if "tomorrow" in text_lower:
        state["date"] = (today + timedelta(days=1)).isoformat()
        return state

    if "today" in text_lower:
        state["date"] = today.isoformat()
        return state

    # fallback to dateparser for things like "next friday"
    parsed = dateparser.parse(
        text,
        settings={
            "PREFER_DATES_FROM": "future",
            "RELATIVE_BASE": datetime.now(),
        },
    )

    if parsed:
        state["date"] = parsed.date().isoformat()

    return state


def planner(state: dict, text: str):
    state = extract_slots(text, state)

    for slot in ["origin", "destination", "date"]:
        if slot not in state:
            return {"action": "ask", "slot": slot}

    return {"action": "execute"}
