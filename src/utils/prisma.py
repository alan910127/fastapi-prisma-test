from prisma import Prisma


async def get_db():
    async with Prisma() as prisma:
        yield prisma
