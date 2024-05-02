from sqlalchemy import Column, String, Integer
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    email = Column(String)
    password = Column(String)

# class UserCreate(BaseModel):
#     full_name: str
#     email: EmailStr
#     password: SecretStr
#     model_config = ConfigDict(populate_by_name=True, json_schema_extra={
#         "example": {
#             "full_name": "Simone Pecora",
#             "email": "simonepecora@live.it",
#             "password": "mypassword"
#         }
#     })

# class UserResponse(BaseModel):
#     id: UUID
#     full_name: str
#     email: EmailStr
#     password: SecretStr