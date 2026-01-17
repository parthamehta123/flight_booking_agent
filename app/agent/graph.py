from app.agent.nodes.planner import planner
from app.agent.nodes.executor import executor
from app.agent.nodes.verifier import verifier
from app.db.factory import get_repository
from app.memory.factory import get_memory


class AgentGraph:
    def __init__(self):
        self.sessions = {}
        self.repo = get_repository()
        self.memory = get_memory()

    async def invoke(self, user_id: str, text: str):
        state = self.sessions.get(user_id, {})

        decision = planner(state, text)

        if decision["action"] == "ask":
            self.sessions[user_id] = state

            slot = decision["slot"]

            if slot == "origin":
                return "Where are you flying from?"
            if slot == "destination":
                return "Where are you flying to?"
            if slot == "date":
                return "When would you like to travel?"
            if slot == "passengers":
                return "How many passengers?"

            return f"Please provide {slot}."

        result = await executor(state)

        if verifier(result):
            self.sessions.pop(user_id, None)
            booking = result["booking"]

            await self.repo.save(booking)
            self.memory.store(
                user_id,
                f"{booking.flight.origin}->{booking.flight.destination}",
            )

            return (
                f"Booked {booking.flight.airline} "
                f"{booking.flight.flight_id} "
                f"for ${booking.flight.price}. "
                f"Confirmation: {booking.booking_id}"
            )

        return "Something went wrong."
