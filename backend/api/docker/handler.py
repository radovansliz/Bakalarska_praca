from python_on_whales import DockerClient
import os
import functools
import asyncio
import multiprocessing
import docker

docker_instance = None


def init_simulator_compose(sim_name: str, user_id: str) -> DockerClient:
    compose_path = os.path.join(
        os.getcwd(), "backend", "simulators", sim_name, "docker-compose.yaml"
    )
    os.system("ls -la")
    os.system("echo skusme")
    os.system("echo " + compose_path)
    os.system("cat " + compose_path)
    docker = DockerClient(compose_files=[compose_path])
    # os.system('cat ' + str(docker))
    # compose_config = docker.compose.config(return_json=True)
    # compose_config.services["simulator_backend"].environment.update(
    #     {"USER_ID": user_id}
    # )
    return docker


def start_simulator_compose():
    docker = DockerClient()
    # Run BE container
    # be_context_path = os.path.join(os.getcwd(),"backend", "simulators", "simulator_1", "backend") # FOR LOCAL NOT FROM DOCKER
    simulator_path = os.path.join(os.getcwd(), "simulators", "simulator_sql")
    print(f"SIMULATOR PATH: ", os.getcwd())
    be_context_path = os.path.join(
        os.getcwd(), "simulators", "simulator_sql", "backend"
    )

    fe_context_path = os.path.join(
        os.getcwd(), "simulators", "smulator_sql", "frontend"
    )

    # TOTO JE POUZIVANY BE IMAGE
    be_image2 = docker.buildx.build(
        be_context_path, platforms=["linux/amd64"], cache=True, tags=["sim_be_latest"]
    )

    # Toto je DB
    db_container = docker.run(
        "postgres",
        name="simulator_database",
        envs={
            "POSTGRES_PASSWORD": "postgres",
            "POSTGRES_DB": "simulator",
            "PGDATA": "/var/lib/postgresql/data",
        },
        publish=[(6544, 5432)],
        # volumes=[
        #     (
        #         "/simulators/simulator_sql/database-data",
        #         "/var/lib/postgresql/data",
        #     ),
        #     (
        #         "/simulators/simulator_sql/sql/create_tables.sql",
        #         "/docker-entrypoint-initdb.d/create_tables.sql",
        #     ),
        #     (
        #         os.path.join(simulator_path + "/sql/insert_data.sql"),
        #         "/docker-entrypoint-initdb.d/insert_data.sql",
        #     ),
        # ],
        detach=True,
        remove=True,
        labels={"source": "simulator_database"},
    )

    # TOTO JE FUNKCNA VERZIA
    be_container = docker.run(
        # platform="linux/amd64",
        image=be_image2,
        # volumes=[(be_volume_path, "/api")],
        # command=["uvicorn api.main:app  --host 0.0.0.0 --port 81"],
        envs={
            "DATABASE_HOST": "database",
            "DATABASE_NAME": "test",
            "DATABASE_USER": "postgres",
            "DATABASE_PASSWORD": "postgres",
            "DATABASE_PORT": 5432,
        },
        publish=[(2001, 81)],
        name="simulator_backend",
        detach=True,
        remove=False,
    )

    print(f"DB CONTAINER: ", db_container)
    print(f"BE COntainer: ", be_container)

    # docker.compose.up(detach=True)

    # Find frontend service container
    # frontend_container = None
    # for container in docker.ps():
    #     if container.name == "simulator_frontend":
    #         frontend_container = container

    # # Find host port in FE container and return it
    # fe_internal_port = frontend_container.args[6]
    # fe_host_port = frontend_container.host_config.port_bindings[
    #     fe_internal_port + "/tcp"
    # ][0].host_port
    return "be_container"
