
# Function to get random number of simulator based on AIS ID seed
def get_random_simulator_select(aisId: int) -> int:
    import random
    random.seed(aisId)
    return random.randint(1, 3)
