from app.config.db import get_session
from fabric.reference_routes.router_fabric import generate_routes_pack, Method

from app import cruds
from app.schemas import (
    user_fabric,
    indicator_fabric,
    poll_fabric,
    vote_fabric,
    schedule_fabric,
)

user_router = generate_routes_pack(
    router_prefix="/users",
    common_name="user",
    crud=cruds.UserCrud(),
    fabric=user_fabric,
    get_session=get_session,
    excluded_methods=[Method.put, Method.patch, Method.csv],
)
indicator_router = generate_routes_pack(
    router_prefix="/indicators",
    common_name="indicator",
    crud=cruds.IndicatorCrud(),
    fabric=indicator_fabric,
    get_session=get_session,
    excluded_methods=[Method.csv],
)
poll_router = generate_routes_pack(
    router_prefix="/polls",
    common_name="poll",
    crud=cruds.PollCrud(),
    fabric=poll_fabric,
    get_session=get_session,
    excluded_methods=[Method.csv],
)
vote_router = generate_routes_pack(
    router_prefix="/votes",
    common_name="vote",
    crud=cruds.VoteCrud(),
    fabric=vote_fabric,
    get_session=get_session,
    excluded_methods=[Method.put, Method.csv],
)
schedule_router = generate_routes_pack(
    router_prefix="/schedules",
    common_name="schedule",
    crud=cruds.ScheduleCrud(),
    fabric=schedule_fabric,
    get_session=get_session,
    excluded_methods=[Method.csv],
)
