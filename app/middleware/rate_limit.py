import time
from fastapi import HTTPException

WINDOW = 60
LIMIT = 5
STORE = {}


def rate_limit(user_id: str):
    now = time.time()
    history = STORE.get(user_id, [])
    history = [t for t in history if now - t < WINDOW]

    if len(history) >= LIMIT:
        raise HTTPException(429, "Too many requests")

    history.append(now)
    STORE[user_id] = history
