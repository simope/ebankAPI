from fastapi import APIRouter, Request, status, Body
from typing import List
from src.models.transfers import Transfer

import src.rules.transfers as transfers

router = APIRouter(prefix="/transfers",
    tags=["Transfers"])

@router.post("/", response_description="Create a new transfer", status_code=status.HTTP_201_CREATED, response_model=Transfer)
def create_user(request: Request, user: Transfer = Body(...)):  
    return transfers.create_transfer(request,user)

# @router.get("/", response_description="List transfers", response_model=List[Transfer])
# def list_users(request: Request):
#     return transfers.list_transfers(request, 100)