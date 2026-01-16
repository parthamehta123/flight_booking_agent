from app.agent.nodes.planner import planner
from app.agent.nodes.executor import executor
from app.agent.nodes.verifier import verifier
from app.db.repository import BookingRepository
from app.memory.vector_store import VectorMemory


class AgentGraph:
    def __init__(self):
        self.sessions = {}
        self.repo = BookingRepository()
        self.memory = VectorMemory()

    async def invoke(self, user_id: str, text: str):
        state = self.sessions.get(user_id, {})

        decision = planner(state, text)

        if decision["action"] == "ask":
            self.sessions[user_id] = state
            return f"Please provide {decision['slot']}."

        result = await executor(state)

        if verifier(result):
            self.sessions.pop(user_id, None)
            booking = result["booking"]

            self.repo.save(booking)
            self.memory.store(
                user_id, f"{booking.flight.origin}->{booking.flight.destination}"
            )

            return (
                f"Booked {booking.flight.airline} "
                f"{booking.flight.flight_id} "
                f"for ${booking.flight.price}. "
                f"Confirmation: {booking.booking_id}"
            )

        return "Something went wrong."
