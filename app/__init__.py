from app import routes
from app.config.api import server, app

app.include_router(routes.user_router)
app.include_router(routes.indicator_router)
app.include_router(routes.poll_router)
app.include_router(routes.vote_router)
app.include_router(routes.schedule_router)