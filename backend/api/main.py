from fastapi import FastAPI
import api.config as config
from .routers import core
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

# CREATE INIT TABLE WITH STUDENTS
db_module.connection = db_module.create_db_connection()
db_module.cursor = db_module.connection.cursor()
# SQL To create table
result = db_module.cursor.execute("""CREATE TABLE STUDENTS(AIS_ID INT NOT NULL, SIMULATOR_NUMBER INT)""")
db_module.connection.commit()