from core.config import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    ADMIN_PASSWORD_HASH,
    ADMIN_USERNAME,
)
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from services.auth import authenticate, create_token

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends()):
    ok = authenticate(
        form.username,
        form.password,
        ADMIN_USERNAME,
        ADMIN_PASSWORD_HASH,
    )

    if not ok:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"sub": form.username}, ACCESS_TOKEN_EXPIRE_MINUTES)

    return {"access_token": token, "token_type": "bearer"}
