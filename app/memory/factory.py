from app.config.settings import settings
from app.memory.vector_store import VectorMemory
from app.memory.in_memory import InMemoryMemory


def get_memory():
    if settings.memory_backend.lower() == "inmemory":
        return InMemoryMemory()

    # default
    return VectorMemory()
