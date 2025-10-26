from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BigInteger, String, Date


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, index=True)
    language: Mapped[str | None] = mapped_column(String(5), nullable=True, default=None)
    gender: Mapped[str | None] = mapped_column(String(10), nullable=True, default=None)
    birth_date: Mapped[Date | None] = mapped_column(Date, nullable=True, default=None)
    last_card_date: Mapped[Date | None] = mapped_column(Date, nullable=True)
    last_obusha_date: Mapped[Date | None] = mapped_column(Date, nullable=True)
    last_vadaram_date: Mapped[Date | None] = mapped_column(Date, nullable=True)
    last_moon_date: Mapped[Date | None] = mapped_column(Date, nullable=True)
