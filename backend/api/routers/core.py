from fastapi import APIRouter, Body, HTTPException
from pydantic import BaseModel, validator
import os

# import api.database.connect as db_module
from api.helpers.simulator import get_random_simulator_select

from api.docker.handler import (
    init_simulator_compose,
    start_simulator_compose,
    docker_instance,
)

router = APIRouter()


class BaseUserModel(BaseModel):
    id: int

    # @validator("id")
    # def ais_id_valid(cls, value):
    #     if not isinstance(value, (int, str)):
    #         raise ValueError("ID must be an int or a str")
    #     if isinstance(value, (str)) and len(id) > 10:
    #         raise ValueError(
    #             "Provided ID is not valid. ID must not be longer than 10 characters"
    #         )
    #     else:
    #         return id
    pass


@router.get("/health")
def healthcheck():
    return {"status": 200, "message": "Alive as never beforee."}


@router.post("/start")
async def start_simulator(user: BaseUserModel = Body(...)):
    try:
        # TEMP INSERTING ID INTO DB...
        # response = db_module.cursor.execute("""INSERT INTO students (ais_id, simulator_number) VALUES (%s, %s)""", (user.id, 1,))
        # result = db_module.cursor.fetchone()
        # db_module.connection.commit()

        # Prevziatie AIS ID
        user_id = user.id

        # Random funkcia vyberie simulator
        simulator = get_random_simulator_select(user_id)

        # Nahranie AIS ID do ENV simulatora
        # docker_instance = init_simulator_compose(simulator, str(user_id))
        # TODO: Spustenie simulatora
        # host_port = start_simulator_compose(docker_instance)
        # simulator_url = "https://localhost:" + host_port
        
        skuska = start_simulator_compose()
        #  print(skuska)

        # TODO: Ulozenie udajov do globalnej DB

        return {
            "user_id": user_id,
            "simulator": simulator,
            "url": "http://localhost:2001",
        }
    except ValueError as e:
        # raise HTTPException(
        #     status_code=400,
        #     detail={
        #         "success": False,
        #         "error": "Given AIS ID is not valid.",
        #         "detail": str(e),
        #     },
        # )
        return {
            "success": False,
            "error": "Given AIS ID is not valid.",
            "detail": str(e),
        }
