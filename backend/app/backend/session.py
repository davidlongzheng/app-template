from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.backend.config import config

# create session factory to generate new database sessions
SessionFactory = async_sessionmaker(
    create_async_engine(config.database.url),
    class_=AsyncSession,
    expire_on_commit=False,
)


async def create_session() -> AsyncGenerator[AsyncSession, None]:
    """Create new database session.

    Yields:
        Database session.
    """

    session = SessionFactory()

    try:
        yield session
        await session.commit()
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()


open_session = asynccontextmanager(create_session)
