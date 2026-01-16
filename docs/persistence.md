# Persistence Layer

This project supports both in-memory and Postgres-backed persistence using the repository pattern.

- Default: In-memory (fast tests, no setup)
- Production: Async Postgres via SQLAlchemy

Configured via environment variables:
USE_POSTGRES=true
DATABASE_URL=postgresql+asyncpg://...