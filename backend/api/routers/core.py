from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field, validator
import api.database.connect as db_module

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
        # TEMP INSERTING ID INTO DB...
        db_module.cursor.execute("""INSERT INTO students (ais_id) VALUES (%s)""", (aisId.id,))
        db_module.connection.commit()
        return aisId
    except Exception as e:
        return {
            "success": False,
            "error": "Given AIS ID is not valid.",
            "detail": str(e)
        }