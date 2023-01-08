from fastapi import APIRouter, Body, HTTPException
from pydantic import BaseModel, validator

router = APIRouter()

@router.get("/health")
def healthcheck():
    return {"status": 200, "message": "Alive as never before."}