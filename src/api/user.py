from fastapi import APIRouter, Depends

from prisma.models import User
from prisma.partials import UserWithoutPassword
from src.auth.deps import get_current_user
from src.utils.prisma import Prisma, get_db

router = APIRouter()


@router.get("/", response_model=list[UserWithoutPassword])
async def get_users(prisma: Prisma = Depends(get_db)):
    return await prisma.user.find_many()


@router.get("/me", response_model=UserWithoutPassword)
async def get_me(user: User = Depends(get_current_user)):
    return user
