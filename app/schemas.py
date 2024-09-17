from app import models
from fabric.common.sqlalchemy_to_pydantic import (
    get_model_schema,
    get_model_identity_schema,
)
from fabric.reference_routes.route_schema import PydanticRouteModelsFabric


UserIdentity = get_model_identity_schema(models.User, include_unique=True)
UserBase = get_model_schema(models.User)

IndicatorIdentity = get_model_identity_schema(
    models.Indicator, include_unique=True
)
IndicatorBase = get_model_schema(models.Indicator)

PollIdentity = get_model_identity_schema(models.Poll, include_unique=True)
PollBase = get_model_schema(models.Poll)

VoteIdentity = get_model_identity_schema(models.Vote, include_unique=True)
VoteBase = get_model_schema(models.Vote)

ScheduleIdentity = get_model_identity_schema(
    models.Schedule, include_unique=True
)
ScheduleBase = get_model_schema(models.Schedule)


user_fabric = PydanticRouteModelsFabric(UserBase, UserIdentity)
indicator_fabric = PydanticRouteModelsFabric(IndicatorBase, IndicatorIdentity)
poll_fabric = PydanticRouteModelsFabric(PollBase, PollIdentity)
vote_fabric = PydanticRouteModelsFabric(VoteBase, VoteIdentity)
schedule_fabric = PydanticRouteModelsFabric(ScheduleBase, ScheduleIdentity)
