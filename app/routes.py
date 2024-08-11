from config.db import get_session
from fabric.reference_routes.router_fabric import generate_routes_pack

from app.cruds import get_user_crud, get_indicator_crud, get_poll_crud
from app.schemas import (
    user_fabric,
    indicator_fabric,
    poll_fabric,
    votes_fabric,
    schedule_fabric,
)

user_router = generate_routes_pack(
    router_prefix="/users",
    common_name="user",
    crud=get_user_crud,
    fabric=user_fabric,
    get_session=get_session,
)
indicator_router = generate_routes_pack(
    router_prefix="/indicator",
    common_name="indicator",
    crud=get_indicator_crud,
    fabric=indicator_fabric,
    get_session=get_session,
)
poll_router = generate_routes_pack(
    router_prefix="/poll",
    common_name="poll",
    crud=get_poll_crud,
    fabric=poll_fabric,
    get_session=get_session,
)
