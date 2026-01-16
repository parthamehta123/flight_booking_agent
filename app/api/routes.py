from fastapi import APIRouter, Depends, HTTPException
from app.db.postgres_repo_async import get_repo

router = APIRouter()


@router.get("/health")
async def health():
    return {"status": "ok"}


@router.get("/bookings/{booking_id}")
async def get_booking(booking_id: str, repo=Depends(get_repo)):
    booking = await repo.get(booking_id)
    if not booking:
        raise HTTPException(404, "Booking not found")

    return {
        "booking_id": booking.booking_id,
        "origin": booking.origin,
        "destination": booking.destination,
        "date": booking.date,
        "passengers": booking.passengers,
        "flight_number": booking.flight_number,
        "price": booking.price,
    }
