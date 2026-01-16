from app.config.settings import settings
from app.db.memory_repo import InMemoryBookingRepository

_repo = None


def get_repository():
    global _repo

    if _repo is not None:
        return _repo

    # Default safe mode
    if not settings.use_postgres:
        _repo = InMemoryBookingRepository()
        return _repo

    # Lazy import: only when enabled
    from app.db.postgres_repo_async import AsyncPostgresBookingRepository

    _repo = AsyncPostgresBookingRepository()
    return _repo
