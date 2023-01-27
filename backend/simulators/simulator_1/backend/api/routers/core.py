from fastapi import APIRouter, Body, HTTPException
from pydantic import BaseModel, validator
from api.database.connect import execute_query
from api.routers.helpers import find_object_in_payload

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
    results = []
    for object in payload.form:
        try:
            result = None
            if int(object.id) == 1:
                # Vulnerable to SQL Injection
                query = f"SELECT * FROM clients WHERE name = '{find_object_in_payload(payload, object.name)}"
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
