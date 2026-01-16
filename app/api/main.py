from fastapi import FastAPI, HTTPException, Request, Depends
from pydantic import BaseModel

from app.agent.graph import AgentGraph
from app.db.factory import get_repository
from app.middleware import setup_middleware
from app.auth import verify_token
from app.limiter import limiter
from app.config.settings import settings


app = FastAPI(title=settings.app_name)

graph = AgentGraph()
repo = get_repository()

setup_middleware(app)


class ChatRequest(BaseModel):
    user_id: str
    message: str


@app.post("/chat", dependencies=[Depends(verify_token)])
@limiter.limit(settings.rate_limit)
async def chat(req: ChatRequest, request: Request):
    reply = await graph.invoke(req.user_id, req.message)
    return {"reply": reply}


@app.get("/bookings/{booking_id}", dependencies=[Depends(verify_token)])
async def get_booking(booking_id: str):
    booking = await repo.get(booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    return {
        "booking_id": booking.booking_id,
        "origin": booking.origin,
        "destination": booking.destination,
        "date": booking.date,
        "passengers": booking.passengers,
        "flight_number": booking.flight_number,
        "price": booking.price,
    }


@app.get("/health")
async def health():
    return {"status": "ok"}
