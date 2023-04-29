from fastapi import FastAPI
import api.config as config
from api.routers import core
from fastapi.middleware.cors import CORSMiddleware
from api.database.connect import init_db_students_table
import os

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

# Set environment variable - current path to project
os.environ["USER_PROJECT_PATH"] = "/Users/radovansliz/Bakalarka/Bakalarska_praca"

# CREATE INIT TABLE WITH STUDENTS
init_db_students_table()
