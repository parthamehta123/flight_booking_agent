import uuid
import time
import logging
from fastapi import Request

logger = logging.getLogger("api")
logging.basicConfig(level=logging.INFO)


async def logging_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())
    start = time.time()

    response = await call_next(request)

    duration = round((time.time() - start) * 1000, 2)

    logger.info(
        f"{request.method} {request.url.path} "
        f"status={response.status_code} "
        f"duration_ms={duration} "
        f"request_id={request_id}"
    )

    response.headers["X-Request-ID"] = request_id
    return response
