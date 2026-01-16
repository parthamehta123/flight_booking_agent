from app.models.domain import Booking


class BookingRepository:
    async def save(self, booking: Booking):
        raise NotImplementedError

    async def get(self, booking_id: str):
        raise NotImplementedError
