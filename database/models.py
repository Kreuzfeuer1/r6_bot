from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    ...


class Team(Base):
    __tablename__ = 'team'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(32), nullable=False)
    first_player: Mapped[str] = mapped_column(String(32), nullable=False)
    second_player: Mapped[str] = mapped_column(String(32), nullable=False)
    third_player: Mapped[str] = mapped_column(String(32), nullable=False)
    fourth_player: Mapped[str] = mapped_column(String(32), nullable=False)
    fifth_player: Mapped[str] = mapped_column(String(32), nullable=False)
    coach: Mapped[str] = mapped_column(String(32), nullable=False)
    logo: Mapped[str] = mapped_column(String(150))