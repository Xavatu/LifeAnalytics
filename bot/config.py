import os

API_HOST = os.getenv("API_HOST", "localhost")
API_PORT = os.getenv("API_PORT", "8000")
API_PORT = int(API_PORT)
BOT_TOKEN = os.getenv("BOT_TOKEN")
