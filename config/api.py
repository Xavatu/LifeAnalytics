import os

import uvicorn
from fastapi import FastAPI

host = os.getenv("API_HOST", "localhost")
port = os.getenv("API_PORT", "8000")
port = int(port)

app = FastAPI(title="LifeAnalytics")
config = uvicorn.Config(app, host=host, port=port)
server = uvicorn.Server(config)
