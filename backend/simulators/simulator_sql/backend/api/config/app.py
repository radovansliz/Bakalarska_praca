import os

APP_ENV: str = os.getenv("APP_ENV", "local")
VERSION: str = os.getenv("VERSION", "0.0.1")