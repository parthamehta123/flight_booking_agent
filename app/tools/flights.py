import random
import asyncio
from app.models.domain import Flight


async def search_flights(origin: str, destination: str, date: str, passengers: int):
    await asyncio.sleep(0.1)
    return [
        Flight(
            flight_id=f"FL{random.randint(1000,9999)}",
            airline=random.choice(["Delta", "United", "JetBlue"]),
            price=random.randint(120, 450),
            origin=origin,
            destination=destination,
            date=date,
        )
        for _ in range(3)
    ]
