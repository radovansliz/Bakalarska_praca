from fastapi import FastAPI
import api.config as config
from api.routers import core
from fastapi.middleware.cors import CORSMiddleware
import api.database.connect as db_module

app = FastAPI(
    docs_url=config.APP_ENV == "local" if "/docs" else None,
    redoc_url=None,
    openapi_url=None,
)

app.include_router(core.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
