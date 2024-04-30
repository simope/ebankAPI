from fastapi import Request, Body
from fastapi.encoders import jsonable_encoder
from src.models.users import User


def get_collection_users(request: Request):
    return request.app.database["users"]


def create_user(request: Request, user: User = Body(...)):
    user = jsonable_encoder(user)
    new_user = get_collection_users(request).insert_one(user)
    created_user = get_collection_users(request).find_one({"_id": new_user.inserted_id})
    return created_user

def list_users(request: Request, limit: int):
    users = list(get_collection_users(request).find(limit=limit))
    return users