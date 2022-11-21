from fastapi import APIRouter

from . import user

api = APIRouter()
api.include_router(user.router, prefix="/user", tags=["user"])
