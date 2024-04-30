from fastapi import APIRouter, Request, status, Body
from typing import List
from src.models.users import User

import src.rules.users as users

router = APIRouter(prefix="/users",
    tags=["Users"])

@router.post("/", response_description="Create a new user", status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(request: Request, user: User = Body(...)):  
    return users.create_user(request,user)

@router.get("/", response_description="List users", response_model=List[User])
def list_users(request: Request):
    return users.list_users(request, 100)