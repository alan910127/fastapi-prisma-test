from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

from prisma import Prisma
from prisma.partials import UserWithoutId, UserWithoutPassword
from src.utils.prisma import get_db

from . import utils

router = APIRouter()


class Token(BaseModel):
    access_token: str
    refresh_token: str


@router.post("/signup", response_model=UserWithoutPassword)
async def create_user(input: UserWithoutId, prisma: Prisma = Depends(get_db)):
    existing_user = await prisma.user.find_unique(where={"username": input.username})

    if existing_user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User {input.username} already exists",
        )

    created_user = await prisma.user.create(
        {
            "username": input.username,
            "password": utils.get_hashed_password(input.password),
            "name": input.name,
            "phone": input.phone,
        }
    )

    return created_user


@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), prisma: Prisma = Depends(get_db)
):
    credential_error = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Incorrect username or password",
    )

    existing_user = await prisma.user.find_unique(
        where={"username": form_data.username}
    )

    if existing_user is None or (
        not utils.verify_password(form_data.password, existing_user.password)
    ):
        raise credential_error

    return Token(
        access_token=utils.create_access_token(existing_user.username),
        refresh_token=utils.create_refresh_token(existing_user.username),
    )
