import asyncio
from app.agent.graph import AgentGraph
from app.config.settings import settings


async def main():
    print("=== Smoke Test ===")
    print("ENV:", settings.env)
    print("USE_POSTGRES:", settings.use_postgres)
    print("MEMORY_BACKEND:", settings.memory_backend)
    print()

    agent = AgentGraph()

    # Run conversation
    print(await agent.invoke("demo", "book me a flight"))
    print(await agent.invoke("demo", "from sfo"))
    print(await agent.invoke("demo", "to jfk tomorrow for 2 people"))

    print("\n=== Memory Check ===")

    # Try to inspect memory content
    memory = agent.memory

    # If in-memory backend
    if hasattr(memory, "store_dict"):
        print("InMemoryMemory contents:", memory.store_dict)

    # If vector backend (Chroma)
    elif hasattr(memory, "collection"):
        try:
            results = memory.collection.get()
            print("VectorMemory (Chroma) contents:")
            for doc in results.get("documents", []):
                print("-", doc)
        except Exception as e:
            print("Could not inspect vector memory:", e)

    else:
        print("Memory backend does not support inspection")


if __name__ == "__main__":
    asyncio.run(main())
