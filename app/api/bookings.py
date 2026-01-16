from fastapi import APIRouter, HTTPException
from app.db.factory import get_repository

router = APIRouter()


@router.get("/bookings/{booking_id}")
async def get_booking(booking_id: str):
    repo = get_repository()
    booking = await repo.get(booking_id)
    if not booking:
        raise HTTPException(404, "Booking not found")
    return booking
