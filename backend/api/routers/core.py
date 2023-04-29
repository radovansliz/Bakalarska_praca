from fastapi import APIRouter, Body
from pydantic import BaseModel
from api.helpers.simulator import get_random_simulator_select
from api.docker.handler import *
from api.database.connect import *

router = APIRouter()
database_simulator_container = None
backend_simulator_container = None
frontend_simulator_container = None
simulator_network = None
docker_client = None


class BaseUserModel(BaseModel):
    id: int
    pass


@router.get("/health")
def healthcheck():
    return {"status": 200, "message": "Alive as never beforee."}


@router.get("/stop")
def stop_simulators():
    try:
        if (
            database_simulator_container != None
            and backend_simulator_container != None
            and frontend_simulator_container != None
        ):
            docker_client.container.stop(
                [
                    frontend_simulator_container,
                    backend_simulator_container,
                    database_simulator_container,
                ]
            )
        if simulator_network != None:
            simulator_network.remove()
        return {"status": 200, "message": "Running simulators stopped and removed"}
    except ValueError as e:
        return {
            "success": False,
            "error": "An error has occured, during removing containers and network",
            "detail": str(e),
        }


@router.post("/start")
async def start_simulator(user: BaseUserModel = Body(...)):
    try:
        # Prevziatie AIS ID
        user_id = user.id

        # Random funkcia vyberie simulator
        simulator = get_random_simulator_select(user_id)
        # Spustenie simulatora
        simulator_instance = start_simulator_compose(simulator, user_id)

        # Use global variables
        global frontend_simulator_container
        global database_simulator_container
        global backend_simulator_container
        global simulator_network
        global docker_client
        frontend_simulator_container = simulator_instance["containers"]["fe"]
        database_simulator_container = simulator_instance["containers"]["db"]
        backend_simulator_container = simulator_instance["containers"]["be"]
        simulator_network = simulator_instance["network"]
        docker_client = simulator_instance["docker_client"]

        # Ulozenie udajov o studentovi do globalnej DB
        insert_student(user.id, simulator)

        return {
            "user_id": user_id,
            "simulator": simulator,
            "url": "http://localhost:3001",
        }
    except ValueError as e:
        return {
            "success": False,
            "error": "Given AIS ID is not valid.",
            "detail": str(e),
        }
