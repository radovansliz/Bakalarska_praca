from python_on_whales import DockerClient
import os

def init_simulator_compose(sim_name: str, user_id: str) -> DockerClient:
    compose_path = os.path.join(os.getcwd(), 'backend', 'simulators', sim_name, 'docker-compose.yaml')
    docker = DockerClient(compose_files=[compose_path])
    compose_config = docker.compose.config(return_json=False)
    compose_config.services["simulator_backend"].environment.update({"USER_ID": user_id})
    print(compose_config.services["simulator_backend"].environment)
    return docker


def start_simulator_compose(docker:DockerClient):
    docker.compose.up()
    print(docker.ps())


