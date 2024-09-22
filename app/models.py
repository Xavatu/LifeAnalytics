from enum import Enum

from sqlalchemy import (
    Column,
    Identity,
    DateTime,
    Integer,
    String,
    ForeignKey,
    func,
    SmallInteger,
)

from app.utils.mixins import TableNameMixin
from app.config.db import Base


class User(Base, TableNameMixin):
    id = Column(Integer, Identity(), primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)


class Indicator(Base, TableNameMixin):
    id = Column(Integer, Identity(), primary_key=True)
    name = Column(String(length=30), unique=True, nullable=False)
    description = Column(String(length=200), nullable=True)


class Poll(Base, TableNameMixin):
    id = Column(Integer, Identity(), primary_key=True)
    indicator_id = Column(
        Integer,
        ForeignKey("indicator.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    message = Column(String, nullable=False)


class Vote(Base, TableNameMixin):
    id = Column(Integer, Identity(), primary_key=True)
    user_id = Column(
        Integer,
        ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    poll_id = Column(
        Integer,
        ForeignKey("poll.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    comment = Column(String, nullable=True)
    grade = Column(SmallInteger, nullable=True)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    voted_at = Column(
        DateTime(timezone=True),
        server_onupdate=func.now(),
        nullable=True,
    )


class Repeat(Enum):
    NO_REPEAT = 0
    REPEAT_DAILY = 1
    REPEAT_WEEKLY = 2


class Schedule(Base, TableNameMixin):
    id = Column(Integer, Identity(), primary_key=True)
    poll_id = Column(
        Integer,
        ForeignKey("poll.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    user_id = Column(
        Integer,
        ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    send_at = Column(
        DateTime(timezone=True),
        nullable=False,
    )
    repeat = Column(
        Integer,
        nullable=False,
        default=0,
    )
