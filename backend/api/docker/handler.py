from python_on_whales import DockerClient
import os

# Method to check if simulator part image exists or need to be built
# Returns image instance
# sim_name = Simulator name - if it's SQL Injection simulator or any other
# service_type = "backend" or "frontend"
def get_simulator_service_image(sim_name: str, service_type: str):
    docker = DockerClient(debug=True)

    # Image has name of simulator
    image_name = sim_name + "_" + service_type + "_image"

    # Initialize empty image
    docker_image = None

    # Check if image is built
    if docker.image.exists(image_name):
        print("Existuje")
        docker_image = docker.image.inspect(image_name)
    else:
        print("Neexistuje")
        # Path to simulator backend code
        context_path = os.path.join(os.getcwd(), "simulators", sim_name, service_type)

        # Build image
        docker_image = docker.buildx.build(
            context_path, platforms=["linux/amd64"], cache=True, tags=[image_name]
        )

    print(docker_image)
    return docker_image


def start_simulator_compose(sim_name: str, userId: int):
    docker = DockerClient(debug=True)

    # Simulator backend image
    sim_be_image = get_simulator_service_image(sim_name, "backend")

    # Simulator frontend image
    sim_fe_image = get_simulator_service_image(sim_name, "frontend")

    # Simulator Database container
    db_volumes = [
        (
            str(os.environ["USER_PROJECT_PATH"])
            + "/backend/simulators/"
            + sim_name
            + "/sql/create_tables.sql",
            # os.path.join(
            #     os.getcwd(), "simulators", sim_name, "sql", "create_tables.sql"
            # ),
            "/docker-entrypoint-initdb.d/create_tables.sql",
        ),
        (
            str(os.environ["USER_PROJECT_PATH"])
            + "/backend/simulators/"
            + sim_name
            + "/sql/insert_data.sql",
            # os.path.join(os.getcwd(), "simulators", sim_name, "sql", "insert_data.sql"),
            "/docker-entrypoint-initdb.d/insert_data.sql",
        ),
    ]
    db_simulator_name = str(userId) + "_" + sim_name + "_" + "database"
    db_container = None

    # Simulator Backend container
    be_simulator_name = str(userId) + "_" + sim_name + "_" + "backend"
    be_container = None

    # Create isolated docker network for simulator specified by simulator name and user's ID
    simulator_docker_network = docker.network.create(str(userId) + "_" + sim_name)

    # Simulator Frontend container
    fe_simulator_name = str(userId) + "_" + sim_name + "_" + "frontend"
    fe_container = None

    # Run containers
    db_container = docker.run(
        "postgres:latest",
        name=db_simulator_name,
        hostname=db_simulator_name,
        envs={
            "POSTGRES_PASSWORD": "postgres",
            "POSTGRES_DB": "simulator",
            "PGDATA": "/var/lib/postgresql/data",
        },
        publish=[(6544, 5432)],
        volumes=db_volumes,
        detach=True,
        remove=True,
        labels={"source": db_simulator_name},
        networks=[simulator_docker_network],
    )

    be_container = docker.run(
        image=sim_be_image,
        name=be_simulator_name,
        hostname=be_simulator_name,
        envs={
            "DATABASE_HOST": db_simulator_name,
            "DATABASE_NAME": "simulator",
            "DATABASE_USER": "postgres",
            "DATABASE_PASSWORD": "postgres",
            "DATABASE_PORT": 5432,
        },
        publish=[(2001, 81)],
        detach=True,
        remove=True,
        labels={"source": be_simulator_name},
        networks=[simulator_docker_network],
    )

    fe_container = docker.run(
        image=sim_fe_image,
        name=fe_simulator_name,
        hostname=fe_simulator_name,
        envs={
            "VITE_AIS_ID": userId,
        },
        publish=[(3001, 3001)],
        detach=True,
        remove=True,
        labels={"source": fe_simulator_name},
        networks=[simulator_docker_network],
    )

    return {
        "status": "done",
        "containers": {"be": be_container, "db": db_container, "fe": fe_container},
        "network": simulator_docker_network,
        "docker_client": docker,
    }
