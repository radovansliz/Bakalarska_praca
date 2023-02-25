from fastapi import APIRouter
from api.database.connect import execute_query

router = APIRouter()


@router.get("/health")
def healthcheck():
    return {"status": 200, "message": "Alive as never before."}


@router.get("/flag")
def get_flag():
    try:
        query = f"SELECT flag FROM flags LIMIT 1;"
        result = execute_query(query)
        return {"result": "Success", "detail": result, "status": 200}
    except Exception as e:
        return {"result": "Error", "detail": e, "status": 500}
