from datetime import datetime

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel, ValidationError

from prisma.models import User
from src.utils.prisma import Prisma, get_db

from . import utils

oauth = OAuth2PasswordBearer(tokenUrl="/login", scheme_name="JWT")


class TokenPayload(BaseModel):
    exp: float
    sub: str


async def get_current_user(
    token: str = Depends(oauth), prisma: Prisma = Depends(get_db)
) -> User:
    try:
        payload = jwt.decode(token, utils.JWT_SECRET_KEY, [utils.ALGORITHM])
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.utcnow():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentails",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = await prisma.user.find_unique(where={"username": token_data.sub})

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )

    return user
