from prisma import Prisma
from prisma.partials import UserWithoutId
from src.auth import utils


async def get_many(prisma: Prisma, take: int | None = None, skip: int | None = None):
    users = await prisma.user.find_many(take=take, skip=skip)
    return users


async def get_by_id(prisma: Prisma, user_id: str):
    user = await prisma.user.find_unique(where={"id": user_id})
    return user


async def get_by_username(prisma: Prisma, username: str):
    user = await prisma.user.find_unique(where={"username": username})
    return user


async def create(prisma: Prisma, data: UserWithoutId):
    created = await prisma.user.create(
        data={
            "username": data.username,
            "password": utils.get_hashed_password(data.password),
            "phone": data.phone,
            "name": data.name,
        }
    )
    return created
