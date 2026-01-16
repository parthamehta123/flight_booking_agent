from app.db.repository import BookingRepository
from app.models.domain import Booking


class InMemoryBookingRepository(BookingRepository):
    def __init__(self):
        self._store = {}

    async def save(self, booking: Booking):
        self._store[booking.booking_id] = booking

    async def get(self, booking_id: str):
        return self._store.get(booking_id)
