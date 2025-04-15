from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import  sessionmaker
from core.config import settings
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_async_engine(settings.DATABASE_URL, echo=settings.DEBUG, future=True)

async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db():
    async  with async_session() as session:
        yield  session