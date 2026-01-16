from fastapi import Header, HTTPException
from app.config.settings import settings


def require_token(x_api_token: str = Header(...)):
    if x_api_token != settings.api_token:
        raise HTTPException(401, "Invalid API token")
