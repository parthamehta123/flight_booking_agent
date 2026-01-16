from fastapi import Header, HTTPException, status
from app.config.settings import settings


async def verify_token(authorization: str = Header(...)):
    """
    Expect header:
        Authorization: Bearer <token>
    """
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Authorization header format",
        )

    token = authorization.replace("Bearer ", "").strip()

    if not settings.api_token:
        raise HTTPException(
            status_code=500,
            detail="API_TOKEN not configured on server",
        )

    if token != settings.api_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )
