import asyncio
from app.agent.graph import AgentGraph


def test_conversation_flow():
    agent = AgentGraph()
    r1 = asyncio.run(agent.invoke("u1", "book me a flight"))
    r2 = asyncio.run(agent.invoke("u1", "from sfo"))
    r3 = asyncio.run(agent.invoke("u1", "to jfk tomorrow for 2 people"))

    assert "Please provide origin." in r1
    assert "Please provide destination." in r2
    assert "Booked" in r3
