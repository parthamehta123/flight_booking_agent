import re
from datetime import datetime, timedelta
import dateparser


def extract_slots(text: str, state: dict) -> dict:
    """
    Deterministic slot extraction using regex + date parsing.
    Acts as a reliable fallback when LLM planner is unavailable.
    """
    text_lower = text.lower()

    # -------------------------
    # Airports (3-letter codes)
    # -------------------------
    match = re.search(r"from\s+([a-z]{3})", text_lower)
    if match:
        state["origin"] = match.group(1).upper()

    match = re.search(r"to\s+([a-z]{3})", text_lower)
    if match:
        state["destination"] = match.group(1).upper()

    # -------------------------
    # Passengers
    # -------------------------
    match = re.search(r"(\d+)\s+(people|passengers|travellers|travelers)", text_lower)
    if match:
        state["passengers"] = int(match.group(1))

    # -------------------------
    # Dates (robust handling)
    # -------------------------
    today = datetime.now().date()

    # Explicit keywords (more reliable than dateparser)
    if "tomorrow" in text_lower:
        state["date"] = (today + timedelta(days=1)).isoformat()
        return state

    if "today" in text_lower:
        state["date"] = today.isoformat()
        return state

    # Fallback to dateparser for phrases like "next friday", "march 10"
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
