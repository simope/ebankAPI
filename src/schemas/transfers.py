from fastapi import Request, Body
from fastapi.encoders import jsonable_encoder
from src.models.transfers import Transfer

def get_collection_transfer(request: Request):
    return request.app.database["transfers"]

def create_transfer(request: Request, transfer: Transfer = Body(...)):
    transfer = jsonable_encoder(transfer)
    new_transfer = get_collection_transfer(request).insert_one(transfer)
    created_transfer = get_collection_transfer(request).find_one({"_id": new_transfer.inserted_id})
    return created_transfer