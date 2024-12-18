from fastapi import APIRouter, Depends, HTTPException, status
from models.schemas import UserBase, UserOut
from utils.auth_utils import create_access_token, get_password_hash, verify_password
from typing import List
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

auth_router = APIRouter(prefix="/auth", tags=["auth"])

users_db = {}

@auth_router.post("/register", response_model=UserOut)
def register(user: UserBase):
    if user.username in users_db:
        raise HTTPException(400, "Username already registered")
    hashed_pw = get_password_hash(user.password)
    users_db[user.username] = {
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed_pw
    }
    return UserOut(username=user.username, email=user.email)

@auth_router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user:
        raise HTTPException(400, "Incorrect username or password")
    if not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(400, "Incorrect username or password")
    access_token_expires = timedelta(minutes=5)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
