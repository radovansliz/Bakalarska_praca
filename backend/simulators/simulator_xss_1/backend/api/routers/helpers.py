
# Function to get random number of input vulnerable to SQL Injection
def get_random_vulnerable_input_number(aisId: int) -> str:
    import random

    random.seed(aisId)
    pick = random.randint(1, 9)
    return pick

def find_object_in_payload(payload, key_to_found:str):
    for object in payload.form:
        if(object.name == key_to_found):
            return object.value or 'Chyba'
