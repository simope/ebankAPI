from pydantic import BaseModel, ConfigDict, EmailStr

class UserBase(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    password: str

    model_config = ConfigDict(from_attributes=True)


class CreateUser(UserBase):
    model_config = ConfigDict(from_attributes=True)