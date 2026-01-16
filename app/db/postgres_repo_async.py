from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from app.db.base import Base
from sqlalchemy import Column, String, Integer

from app.config.settings import settings
from app.models.domain import Booking
from app.db.repository import BookingRepository

DATABASE_URL = settings.database_url or "sqlite+aiosqlite:///./dev.db"

engine = create_async_engine(DATABASE_URL)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def get_session():
    async with SessionLocal() as session:
        yield session


class BookingORM(Base):
    __tablename__ = "bookings"

    booking_id = Column(String, primary_key=True)
    origin = Column(String)
    destination = Column(String)
    date = Column(String)
    passengers = Column(Integer)
    flight_number = Column(String)
    price = Column(Integer)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


class AsyncPostgresBookingRepository(BookingRepository):
    async def save(self, booking: Booking):
        async with SessionLocal() as session:
            obj = BookingORM(
                booking_id=booking.booking_id,
                origin=booking.flight.origin,
                destination=booking.flight.destination,
                date=booking.flight.date,
                passengers=booking.passengers,
                flight_number=booking.flight.flight_id,
                price=booking.flight.price,
            )
            await session.merge(obj)
            await session.commit()

    async def get(self, booking_id: str):
        async with SessionLocal() as session:
            return await session.get(BookingORM, booking_id)
