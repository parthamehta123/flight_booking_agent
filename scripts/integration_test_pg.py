import asyncio
from app.tools.booking import book_flight
from app.models.domain import Flight


async def run():
    f = Flight(
        origin="SFO",
        destination="JFK",
        date="2025-01-20",
        flight_id="FL123",
        airline="TestAir",
        price=100,
    )
    booking = await book_flight(f, 2)
    print("Created:", booking.booking_id)


asyncio.run(run())
