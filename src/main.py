from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from .api import api
from .auth.api import router as auth_router

app = FastAPI(title="FastAPI Prisma Test")


@app.get("/")
async def read_root():
    return RedirectResponse("/docs")


app.include_router(api, prefix="/api")
app.include_router(auth_router, tags=["auth"])
