from sqlalchemy import Column, String, Integer
from app.db.database import Base


class BookingORM(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    origin = Column(String)
    destination = Column(String)
    date = Column(String)
    passengers = Column(Integer)
    flight_number = Column(String)
    price = Column(Integer)
    confirmation = Column(String, unique=True)
