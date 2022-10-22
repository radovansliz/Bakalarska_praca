from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field, validator

router = APIRouter()


class BaseAisIdModel(BaseModel):
    id: int



@router.get("/health")
def healthcheck():
    return {"status": 200, "message": "Alive as never before."}


@router.post("/start")
async def start_simulator(aisId: BaseAisIdModel):
    return aisId