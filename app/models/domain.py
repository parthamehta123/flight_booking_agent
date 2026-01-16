from dataclasses import dataclass


@dataclass
class Flight:
    flight_id: str
    airline: str
    price: int
    origin: str
    destination: str
    date: str


@dataclass
class Booking:
    booking_id: str
    flight: Flight
    passengers: int
