from fastapi import APIRouter, Body
from pydantic import BaseModel
from api.database.connect import execute_query
from api.routers.helpers import find_object_in_payload, get_random__number
import os

router = APIRouter()


class FormField(BaseModel):
    id: str
    name: str
    value: str


class BaseFormModel(BaseModel):
    form: list[FormField]


@router.get("/health")
def healthcheck():
    return {"status": 200, "message": "Alive as never before."}


@router.post("/mortgage-interest")
@router.post("/newsletter")
@router.post("/signin")
def create_object(payload: BaseFormModel = Body(...)):
    is_vulnerable = get_random__number(os.getenv("AIS_ID"), 1, 9)
    vulnerability_type = get_random__number(os.getenv("AIS_ID"), 1, 2)
    results = []
    for object in payload.form:
        try:
            result = None
            if str(object.id) == is_vulnerable:
                # Vulnerable to SQL Injection
                if vulnerability_type == '1':
                    # First vulnerability type: Need to add '; and then type query
                    query = f"SELECT * FROM clients WHERE name = '{find_object_in_payload(payload, object.name)}"
                else:
                    # Second vulnerability type: Need to type query and then add -- to comment all behind
                    query = f"{find_object_in_payload(payload, object.name)} WHERE 1=2;"
                result = execute_query(query)
            else:
                # Not vulnerable to SQL Injection
                query = "SELECT * FROM clients WHERE name = %s"
                result = execute_query(
                    query, (find_object_in_payload(payload, object.name),)
                )
            results.append({"response": result, "input": object.name})
        except Exception as e:
            results.append({"response": e, "input": object.name})
            continue
    return {"results": results}
