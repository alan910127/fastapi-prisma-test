from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

from prisma import Prisma
from prisma.partials import UserWithoutId, UserWithoutPassword
from src.db import user
from src.utils.prisma import get_db

from . import utils

router = APIRouter()


class Token(BaseModel):
    access_token: str
    refresh_token: str


@router.post("/signup", response_model=UserWithoutPassword)
async def create_user(data: UserWithoutId, prisma: Prisma = Depends(get_db)):
    existing_user = await user.get_by_username(prisma, data.username)

    if existing_user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User {data.username} already exists",
        )

    created_user = await user.create(prisma, data)

    return created_user


@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), prisma: Prisma = Depends(get_db)
):
    credential_error = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Incorrect username or password",
    )

    existing_user = await user.get_by_username(prisma, form_data.username)

    if existing_user is None or (
        not utils.verify_password(form_data.password, existing_user.password)
    ):
        raise credential_error

    return Token(
        access_token=utils.create_access_token(existing_user.username),
        refresh_token=utils.create_refresh_token(existing_user.username),
    )
