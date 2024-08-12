import asyncio

from app.config.api import server


async def main():
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
