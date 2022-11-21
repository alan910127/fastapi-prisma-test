import os
from datetime import datetime, timedelta
from typing import Any

from jose import jwt
from passlib.context import CryptContext

ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "dev")
JWT_REFRESH_SECRET_KEY = os.getenv("JWT_REFRESH_SECRET_KEY", "dev")

password_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    return password_ctx.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_ctx.verify(password, hashed_password)


def _create_token(
    subject: str | Any,
    expires_delta: int | None = None,
    *,
    expire_time: int,
    secret_key: str
) -> str:
    if expires_delta is not None:
        expires_in = datetime.utcnow() + timedelta(minutes=expires_delta)
    else:
        expires_in = datetime.utcnow() + timedelta(minutes=expire_time)

    to_encode = {"exp": expires_in, "sub": str(subject)}

    return jwt.encode(to_encode, secret_key, ALGORITHM)


def create_access_token(subject: str | Any, expires_delta: int | None = None) -> str:
    return _create_token(
        subject,
        expires_delta,
        expire_time=ACCESS_TOKEN_EXPIRE_MINUTES,
        secret_key=JWT_SECRET_KEY,
    )


def create_refresh_token(subject: str | Any, expires_delta: int | None = None) -> str:
    return _create_token(
        subject,
        expires_delta,
        expire_time=REFRESH_TOKEN_EXPIRE_MINUTES,
        secret_key=JWT_REFRESH_SECRET_KEY,
    )
