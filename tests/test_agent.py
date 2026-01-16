from app.agent.graph import AgentGraph
import pytest


@pytest.mark.asyncio
async def test_conversation_flow():
    agent = AgentGraph()

    r1 = await agent.invoke("u1", "book me a flight")
    r2 = await agent.invoke("u1", "from sfo")
    r3 = await agent.invoke("u1", "to jfk tomorrow for 2 people")

    assert "Where are you flying from?" in r1
    assert "Where are you flying to?" in r2
    assert "Booked" in r3
