from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy_utils import create_database, database_exists

from config import settings

sync_engine = create_engine(url=settings.database_url, future=True, echo=True)
async_engine = create_async_engine(url=settings.async_database_url, future=True, echo=True)
async_session = sessionmaker(bind=async_engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()


if not database_exists(settings.database_url):
    create_database(settings.database_url)


async def get_db():
    db: AsyncSession = async_session()
    try:
        yield db
    finally:
        await db.close()