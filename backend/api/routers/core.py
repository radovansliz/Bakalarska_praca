from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/health")
def healthcheck():
    return {"status": 200, "message": "Alive as never before."}
