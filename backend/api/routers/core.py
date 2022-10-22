from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field, validator

router = APIRouter()


class BaseAisIdModel(BaseModel):
    id: int



@router.get("/health")
def healthcheck():
    return {"status": 200, "message": "Alive as never before."}



@router.post("/initialize/{ais_id}")
async def url_upload(ais_id: str):
    return {"success": True, "id": ais_id}


@router.post("/start")
async def start_simulator(aisId: BaseAisIdModel):
    print("FICI TO")
    print(aisId)
    return aisId