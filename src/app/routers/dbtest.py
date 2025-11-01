from fastapi import APIRouter
from ..db import ping_db

router = APIRouter()

@router.get("/db/ping")
def db_ping():
    return {"ok": ping_db()}
