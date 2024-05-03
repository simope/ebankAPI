from fastapi import Depends, APIRouter, status, HTTPException, Response
from sqlalchemy.orm import Session
from src.schemas.users import CreateUser
from src.models.users import User
from database import get_db


router = APIRouter(prefix="/users",
    tags=["Users"])

# GET ALL
@router.get("/")
def list_users(db: Session = Depends(get_db)):
    all_users = db.query(User).all()
    return all_users

# GET ONE
@router.get("/{id}")
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            details=f"User with such id not found")
    else:
        return user

# POST
@router.post(
        "/",
        response_description="Create a new user",
        status_code=status.HTTP_201_CREATED,
        response_model=CreateUser
        )
def create_user(user_user: CreateUser, db: Session = Depends(get_db)):
    new_user = User(**user_user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# PUT
@router.put("/{id}")
def update_user(id: int, user: CreateUser, db:Session = Depends(get_db)):
    updated_user = db.query(User).filter(User.id == id)
    if updated_user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with such id: {id} does not exist')
    else:
        updated_user.update(user.model_dump(), synchronize_session=False)
        db.commit()
    return updated_user.first()

# DELETE
@router.delete(
        "/{id}",
        status_code=status.HTTP_204_NO_CONTENT
        )
def delete_user(id: int, db: Session = Depends(get_db)):
    delete_post = db.query(User).filter(User.id == id)
    if delete_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            details=f"User with such id not found")
    else:
        delete_post.delete(synchronize_session=False)
        db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)