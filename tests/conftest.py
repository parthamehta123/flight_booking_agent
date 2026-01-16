import asyncio
import pytest_asyncio
import pytest
from httpx import AsyncClient
from testcontainers.postgres import PostgresContainer


from app.api.main import app
from app.db.postgres_repo_async import engine, Base


@pytest_asyncio.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session")
def postgres_container():
    with PostgresContainer("postgres:15") as postgres:
        yield postgres


@pytest_asyncio.fixture(scope="session", autouse=True)
async def prepare_database(postgres_container):
    # Reconfigure engine to test DB
    test_url = postgres_container.get_connection_url().replace(
        "postgresql://", "postgresql+asyncpg://"
    )

    engine.url = test_url

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

        yield

        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
