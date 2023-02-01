from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from config import settings

from sources import db


router = APIRouter()


@router.get("/", response_class=JSONResponse)
async def root(request: Request):
    return {"ok": True}
