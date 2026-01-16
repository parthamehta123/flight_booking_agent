import random
import asyncio
from app.models.domain import Booking, Flight


async def book_flight(flight: Flight, passengers: int):
    await asyncio.sleep(0.05)
    return Booking(
        booking_id=f"CONF{random.randint(100000,999999)}",
        flight=flight,
        passengers=passengers,
    )
