from typing import TypedDict


class AgentState(TypedDict, total=False):
    origin: str
    destination: str
    date: str
    passengers: int
