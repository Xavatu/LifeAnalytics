from pydantic import BaseModel, create_model, ConfigDict

from app import models
from fabric.common.sqlalchemy_to_pydantic import (
    get_model_schema,
    get_model_identity_schema,
)
from fabric.reference_routes.route_schema import PydanticRouteModelsFabric


FromAttributesConfig = lambda: ConfigDict(from_attributes=True)
field_list = lambda _model: list(_model.model_fields.keys())


def copy_schema(
    base_schema: type[BaseModel],
    name: str = None,
    exclude: list[str] = None,
    config: ConfigDict = None,
) -> type[BaseModel]:
    exclude = exclude if exclude else []
    config = config if config else FromAttributesConfig()
    fields = {
        k: (v.annotation, v)
        for k, v in base_schema.model_fields.items()
        if k not in exclude
    }
    name = name if name else base_schema.__name__
    return create_model(name, __config__=config, **fields)


UserIdentity = get_model_identity_schema(models.User, include_unique=True)
UserBase = get_model_schema(models.User)
UserQuery = copy_schema(
    UserBase, name="UserQuery", exclude=field_list(UserIdentity)
)
UserCreate = copy_schema(UserBase, name="UserCreate", exclude=["id"])

IndicatorIdentity = get_model_identity_schema(
    models.Indicator, include_unique=True
)
IndicatorBase = get_model_schema(models.Indicator)
IndicatorQuery = copy_schema(
    IndicatorBase,
    name="IndicatorQuery",
    exclude=[*field_list(IndicatorIdentity), "description"],
)
IndicatorCreate = copy_schema(
    IndicatorBase, name="IndicatorCreate", exclude=["id"]
)

PollIdentity = get_model_identity_schema(models.Poll, include_unique=True)
PollBase = get_model_schema(models.Poll)
PollQuery = copy_schema(
    PollBase,
    name="PollQuery",
    exclude=[*field_list(PollIdentity), "message"],
)
PollCreate = copy_schema(PollBase, name="PollCreate", exclude=["id"])

VoteIdentity = get_model_identity_schema(models.Vote, include_unique=True)
VoteBase = get_model_schema(models.Vote)
VoteQuery = copy_schema(
    VoteBase,
    name="VoteQuery",
    exclude=[*field_list(VoteIdentity), "comment"],
)
VoteCreate = copy_schema(VoteBase, name="VoteCreate", exclude=["id"])

ScheduleIdentity = get_model_identity_schema(
    models.Schedule, include_unique=True
)
ScheduleBase = get_model_schema(models.Schedule)
ScheduleQuery = copy_schema(
    ScheduleBase,
    name="ScheduleQuery",
    exclude=[*field_list(ScheduleIdentity), "comment"],
)
ScheduleCreate = copy_schema(
    ScheduleBase, name="ScheduleCreate", exclude=["id"]
)


user_fabric = PydanticRouteModelsFabric(
    UserBase, UserIdentity, query_class=UserQuery, create_class=UserCreate
)
indicator_fabric = PydanticRouteModelsFabric(
    IndicatorBase,
    IndicatorIdentity,
    query_class=IndicatorQuery,
    create_class=IndicatorCreate,
)
poll_fabric = PydanticRouteModelsFabric(
    PollBase, PollIdentity, query_class=PollQuery, create_class=PollCreate
)
vote_fabric = PydanticRouteModelsFabric(
    VoteBase, VoteIdentity, query_class=VoteQuery, create_class=VoteCreate
)
schedule_fabric = PydanticRouteModelsFabric(
    ScheduleBase,
    ScheduleIdentity,
    query_class=ScheduleQuery,
    create_class=ScheduleCreate,
)
