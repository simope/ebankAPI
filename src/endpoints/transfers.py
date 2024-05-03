from fastapi import Depends, APIRouter, status, HTTPException, Response
from sqlalchemy.orm import Session
from src.schemas.transfers import CreateTransfer
from src.models.transfers import Transfer
from src.models.users import User
from database import get_db


router = APIRouter(prefix="/transfers",
    tags=["Transfers"])

# GET ALL
@router.get("/")
def list_transfers(db: Session = Depends(get_db)):
    all_transfers = db.query(Transfer).all()
    return all_transfers

# GET ONE
@router.get("/{id}")
def get_transfer(id: int, db: Session = Depends(get_db)):
    transfer = db.query(Transfer).filter(Transfer.id == id).first()
    if transfer == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            details=f"Transfer with such id not found")
    else:
        return transfer

# PUT
@router.put("/{id}")
def update_transfer(id: int, user: CreateTransfer, db:Session = Depends(get_db)):
    updated_transfer = db.query(Transfer).filter(Transfer.id == id)
    if updated_transfer == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'transfer with such id: {id} does not exist')
    else:
        updated_transfer.update(user.model_dump(), synchronize_session=False)
        db.commit()
    return updated_transfer.first()

# POST
@router.post(
        "/",
        response_description="Create a new transfer",
        status_code=status.HTTP_201_CREATED,
        response_model=CreateTransfer
        )
def create_transfer(transfer_transfer: CreateTransfer, db: Session = Depends(get_db)):
    new_transfer = Transfer(**transfer_transfer.model_dump())
    db.add(new_transfer)
    db.commit()
    db.refresh(new_transfer)
    return new_transfer

# DELETE
@router.delete(
        "/{id}",
        status_code=status.HTTP_204_NO_CONTENT
        )
def delete_transfer(id: int, db: Session = Depends(get_db)):
    deleted_transfer = db.query(Transfer).filter(Transfer.id == id)
    if deleted_transfer == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            details=f"Transfer with such id not found")
    else:
        deleted_transfer.delete(synchronize_session=False)
        db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)