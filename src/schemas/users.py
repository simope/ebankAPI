from pydantic import BaseModel, ConfigDict, EmailStr

class UserBase(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    password: str

    model_config = ConfigDict(from_attributes=True)


class CreateUser(UserBase):
    model_config = ConfigDict(from_attributes=True)

# def create_user(user: User, db):
#     db_item = User(**user.dict())
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item

# def list_users(request: Request):
#     connection = create_connection()
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM users")
#     answer = cursor.fetchall()
#     output = []
#     for row in answer:
#         output.append({
#             "id": row[0],
#             "full_name": row[1],
#             "email": row[2],
#             "password": row[3]
#             })
#     connection.commit()
#     connection.close()
#     print(output)
#     return output

# def find_user(request: Request, id: UUID):
#     if (user := get_collection_users(request).find_one({"_id": id})):
#         return user
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found.")

# def update_user(request: Request, id: UUID, user: User = Body(...)):
#     update_result = get_collection_users(request).update_one({"_id": id}, {"$set": user})
    
#     if update_result.modified_count == 0:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found.")

#     if (existing_user := get_collection_users(request).find_one({"_id": user.id})) is not None:
#         return existing_user

# def delete_user(request: Request, id: UUID):
#     deleted_user = get_collection_users(request).delete_one({"_id": id})

#     if deleted_user.deleted_count == 1:
#         return f"User with id {id} deleted sucessfully."

#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found.")