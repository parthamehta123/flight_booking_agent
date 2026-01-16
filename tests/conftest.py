import pytest_asyncio
from testcontainers.postgres import PostgresContainer
from sqlalchemy.ext.asyncio import create_async_engine
import httpx
from app.api.main import app
from app.db.base import Base
from sqlalchemy.ext.asyncio import async_sessionmaker


@pytest_asyncio.fixture(scope="session")
def postgres_container():
    with (
        PostgresContainer("postgres:15")
        .with_env("POSTGRES_USER", "test")
        .with_env("POSTGRES_PASSWORD", "test")
        .with_env("POSTGRES_DB", "test")
    ) as postgres:
        yield postgres


@pytest_asyncio.fixture(scope="function", autouse=True)
async def prepare_database(postgres_container):
    import app.db.postgres_repo_async as db
    import app.api.main as main

    test_url = (
        f"postgresql+asyncpg://"
        f"{postgres_container.username}:"
        f"{postgres_container.password}@"
        f"{postgres_container.get_container_host_ip()}:"
        f"{postgres_container.get_exposed_port(5432)}/"
        f"{postgres_container.dbname}"
    )

    test_engine = create_async_engine(test_url, echo=False)

    async_session = async_sessionmaker(
        test_engine,
        expire_on_commit=False,
    )

    # override the session factory used by repository
    db.SessionLocal = async_session

    # rebuild repo using the overridden SessionLocal
    main.repo = db.AsyncPostgresBookingRepository()

    # create tables
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    # cleanup
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    await test_engine.dispose()


@pytest_asyncio.fixture
async def client():
    transport = httpx.ASGITransport(app=app)

    async with httpx.AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as ac:
        yield ac
