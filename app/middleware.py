import uuid
import logging
from fastapi import Request

logger = logging.getLogger("app")
logging.basicConfig(level=logging.INFO)


def setup_middleware(app):
    @app.middleware("http")
    async def add_request_id(request: Request, call_next):
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id

        logger.info(
            f"request_id={request_id} method={request.method} path={request.url.path}"
        )

        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        return response
