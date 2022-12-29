import docker
from python_on_whales import *

# docker.run(
#     "postgres:9.6",
#     name="some-postgres",
#     envs={"POSTGRES_PASSWORD": "mysecretpassword"},
#     detach=True,
# )
# print(docker.ps())

def init_simulator_compose(sim_name:str, user_id: str):
    compose_path = "../../simulators/{0}/docker-compose.yaml".format(sim_name)
    docker = DockerClient(compose_files=[compose_path])
    compose_config = docker.compose.config(return_json=False)
    compose_config.services["backend-api"].environment.update({"USER_ID": user_id})
    print(compose_config.services["backend-api"].environment)
