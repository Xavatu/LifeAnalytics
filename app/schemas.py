from pydantic import Field, constr
from typing import Optional
from enum import Enum
from datetime import datetime, timezone

from fabric.reference_routes.route_schema import (
    BasePydanticClass,
    PydanticRouteModelsFabric,
)


class UserIdentifierType(str, Enum):
    id = "id"
    telegram_id = "telegram_id"


class UserBase(BasePydanticClass):
    telegram_id: int


class IndicatorBaseIdentifierType(str, Enum):
    id = "id"
    name = "name"


class IndicatorBase(BasePydanticClass):
    name: constr(min_length=1, max_length=30)
    description: Optional[constr(min_length=1, max_length=200)]


class PollIdentifierType(str, Enum):
    id = "id"


class PollBase(BasePydanticClass):
    indicator_id: int
    message: constr(min_length=1)


class VoteIdentifierType(str, Enum):
    id = "id"


class VoteBase(BasePydanticClass):
    user_id: int
    poll_id: int
    comment: Optional[str]
    grade: Optional[int] = Field(None, ge=0, le=10)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    voted_at: Optional[datetime] = None


class ScheduleIdentifierType(str, Enum):
    id = "id"


class ScheduleBase(BasePydanticClass):
    poll_id: int
    user_id: int
    send_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


user_fabric = PydanticRouteModelsFabric(UserBase, UserIdentifierType)
indicator_fabric = PydanticRouteModelsFabric(
    IndicatorBase, IndicatorBaseIdentifierType
)
poll_fabric = PydanticRouteModelsFabric(PollBase, PollIdentifierType)
vote_fabric = PydanticRouteModelsFabric(VoteBase, VoteIdentifierType)
schedule_fabric = PydanticRouteModelsFabric(
    ScheduleBase, ScheduleIdentifierType
)
