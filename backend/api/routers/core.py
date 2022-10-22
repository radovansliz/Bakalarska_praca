from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field, validator

router = APIRouter()


class BaseAisIdModel(BaseModel):
    id: int

    @validator("id")
    def ais_id_valid(cls, id):
        if len(str(id)) >= 5 and len(str(id)) < 7:
            return id
        else:
            raise ValueError("Provided AIS ID is not valid")



@router.get("/health")
def healthcheck():
    return {"status": 200, "message": "Alive as never before."}


@router.post("/start")
async def start_simulator(aisId: BaseAisIdModel):
    try:
        BaseAisIdModel(aisId)
        return aisId
    except Exception as e:
        return {
            "success": False,
            "error": "Given AIS ID is not valid.",
            "detail": str(e)
        }