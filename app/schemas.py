from pydantic import BaseModel, create_model, ConfigDict

from app import models
from fabric.common.sqlalchemy_to_pydantic import (
    get_model_schema,
    get_model_identity_schema,
)
from fabric.reference_routes.route_schema import PydanticRouteModelsFabric


FromAttributesConfig = lambda: ConfigDict(from_attributes=True)
field_list = lambda _model: list(_model.model_fields.keys())


def schema_copy(
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
UserQuery = schema_copy(
    UserBase, name="UserQuery", exclude=field_list(UserIdentity)
)

IndicatorIdentity = get_model_identity_schema(
    models.Indicator, include_unique=True
)
IndicatorBase = get_model_schema(models.Indicator)
IndicatorQuery = schema_copy(
    IndicatorBase,
    name="IndicatorQuery",
    exclude=[*field_list(IndicatorIdentity), "description"],
)

PollIdentity = get_model_identity_schema(models.Poll, include_unique=True)
PollBase = get_model_schema(models.Poll)
PollQuery = schema_copy(
    PollBase,
    name="PollQuery",
    exclude=[*field_list(PollIdentity), "message"],
)

VoteIdentity = get_model_identity_schema(models.Vote, include_unique=True)
VoteBase = get_model_schema(models.Vote)
VoteQuery = schema_copy(
    VoteBase,
    name="VoteQuery",
    exclude=[*field_list(VoteIdentity), "comment"],
)

ScheduleIdentity = get_model_identity_schema(
    models.Schedule, include_unique=True
)
ScheduleBase = get_model_schema(models.Schedule)
ScheduleQuery = schema_copy(
    ScheduleBase,
    name="ScheduleQuery",
    exclude=[*field_list(ScheduleIdentity), "comment"],
)


user_fabric = PydanticRouteModelsFabric(
    UserBase, UserIdentity, query_class=UserQuery
)
indicator_fabric = PydanticRouteModelsFabric(
    IndicatorBase, IndicatorIdentity, query_class=IndicatorQuery
)
poll_fabric = PydanticRouteModelsFabric(
    PollBase, PollIdentity, query_class=PollQuery
)
vote_fabric = PydanticRouteModelsFabric(
    VoteBase, VoteIdentity, query_class=VoteQuery
)
schedule_fabric = PydanticRouteModelsFabric(
    ScheduleBase, ScheduleIdentity, query_class=ScheduleQuery
)
