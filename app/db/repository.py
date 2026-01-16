from app.models.domain import Booking


class BookingRepository:
    def __init__(self):
        self._store = {}

    def save(self, booking: Booking):
        self._store[booking.booking_id] = booking

    def get(self, booking_id: str):
        return self._store.get(booking_id)
