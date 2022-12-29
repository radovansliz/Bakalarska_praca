from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field, validator
# import api.database.connect as db_module
from api.helpers.simulator import get_random_simulator_select
from api.docker.handler import init_simulator_compose
router = APIRouter()


class BaseUserModel(BaseModel):
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
async def start_simulator(user: BaseUserModel):
    try:
        # TEMP INSERTING ID INTO DB...
        # response = db_module.cursor.execute("""INSERT INTO students (ais_id, simulator_number) VALUES (%s, %s)""", (user.id, 1,))
        # result = db_module.cursor.fetchone()
        # db_module.connection.commit()
        
        # Prevziatie AIS ID
        user_id = user

        #Random funkcia vyberie simulator
        simulator = get_random_simulator_select(user_id)

        #Nahranie AIS ID do ENV simulatora
        init_simulator_compose(simulator, str(user_id))

        # TODO: Spustenie simulatora

        # TODO: Ulozenie udajov do globalnej DB
        
        # print(response)
        # return response
        return simulator
    except Exception as e:
        return {
            "success": False,
            "error": "Given AIS ID is not valid.",
            "detail": str(e)
        }