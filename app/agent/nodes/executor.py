from app.tools.flights import search_flights
from app.tools.booking import book_flight


async def executor(state: dict):
    flights = await search_flights(
        state["origin"],
        state["destination"],
        state["date"],
        state.get("passengers", 1),
    )
    chosen = min(flights, key=lambda f: f.price)
    booking = await book_flight(chosen, state.get("passengers", 1))
    return {"flight": chosen, "booking": booking}
