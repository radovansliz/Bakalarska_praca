
import random

# Function to get random number used for selection of type of SQL injection as vulnerability or input number vulnerable to SQL Injection
def get_random__number(aisId: int, rangeStart:int, rangeEnd:int) -> str:
    random.seed(aisId)
    pick = random.randint(rangeStart, rangeEnd)
    return str(pick)

def find_object_in_payload(payload, key_to_found:str):
    for object in payload.form:
        if(object.name == key_to_found):
            return object.value or 'Chyba'
