from functools import lru_cache
from fabric.common.crud import CRUDBase

from app.models import User, Indicator, Poll
from app.schemas import UserBase, IndicatorBase, PollBase


class UserCrud(CRUDBase[User, UserBase]):
    ...


@lru_cache(None)
def get_user_crud():
    return UserCrud(User)


class IndicatorCrud(CRUDBase[Indicator, IndicatorBase]):
    ...


@lru_cache(None)
def get_indicator_crud():
    return IndicatorCrud(Indicator)


class PollCrud(CRUDBase[Poll, PollBase]):
    ...


@lru_cache(None)
def get_poll_crud():
    return PollCrud(Poll)
