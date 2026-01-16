import random
import asyncio
from app.models.domain import Booking, Flight
from app.db.factory import get_repository

repo = get_repository()


async def book_flight(flight: Flight, passengers: int):
    await asyncio.sleep(0.05)

    booking = Booking(
        booking_id=f"CONF{random.randint(100000, 999999)}",
        flight=flight,
        passengers=passengers,
    )

    await repo.save(booking)
    return booking
