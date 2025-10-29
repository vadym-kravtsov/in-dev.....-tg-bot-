from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from database.models import Base
from config.settings import DATABASE_URL

db_url = DATABASE_URL.replace('postgres://', 'postgresql+asyncpg://', 1).split('?')[0]

engine = create_async_engine(db_url)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def reset_db_once():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)