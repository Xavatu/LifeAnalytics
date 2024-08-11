import asyncio

from config.api import server, app
from app.routes import user_router, indicator_router, poll_router

app.include_router(user_router)
app.include_router(indicator_router)
app.include_router(poll_router)


async def main():
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
