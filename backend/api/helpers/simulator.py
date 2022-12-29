import random

simulators = ["simulator_1"]

# Function to get random number of simulator based on AIS ID seed and return simulator name
def get_random_simulator_select(aisId: int) -> str:
    random.seed(aisId)
    sim_num = len(simulators)
    pick = random.randint(1, sim_num)
    selected_simulator = simulators[pick - 1]
    return selected_simulator
