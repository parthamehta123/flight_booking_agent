import asyncio
from app.agent.graph import AgentGraph


async def main():
    agent = AgentGraph()

    print(await agent.invoke("demo", "book me a flight"))
    print(await agent.invoke("demo", "from sfo"))
    print(await agent.invoke("demo", "to jfk tomorrow for 2 people"))


if __name__ == "__main__":
    asyncio.run(main())
