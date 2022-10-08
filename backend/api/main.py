from fastapi import FastAPI
import api.config as config
from .routers import core


app = FastAPI(
    docs_url=config.APP_ENV == "local" if "/docs" else None,
    redoc_url=None,
    openapi_url=None,
)

app.include_router(core.router)
