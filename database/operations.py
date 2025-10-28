from sqlalchemy import select
from .database import SessionLocal
from .models import User

async def get_or_create_user(telegram_id: int) -> User:
    async with SessionLocal() as session:
        result = await session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        user = result.scalar_one_or_none()

        if not user:
            user = User(telegram_id=telegram_id)
            session.add(user)
            await session.commit()
            await session.refresh(user)

        return user


async def update_user(telegram_id: int, **kwargs) -> User | None:
    async with SessionLocal() as session:
        result = await session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        user = result.scalar_one_or_none()

        if user:
            for field, value in kwargs.items():
                if hasattr(user, field):
                    setattr(user, field, value)
            await session.commit()
            return user
        else:
            return None


async def get_users_all() -> list[User]:
    async with SessionLocal() as session:
        result = await session.execute(select(User))
        user_obj = result.scalars().all()
        return user_obj


async def update_user_last_message_id(telegram_id: int, message_id: int) -> None:
    async with SessionLocal() as session:
        result = await session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        user = result.scalar_one_or_none()
        if user:
            user.last_message_id = message_id
            await session.commit()