from uuid import uuid4, UUID
from pydantic import BaseModel, Field, SecretStr
from pydantic.networks import EmailStr

class User(BaseModel):
    id: UUID = Field(default_factory=uuid4, alias="_id")
    full_name: str
    email: EmailStr = Field(unique=True, index=False)
    password: SecretStr

    class Config:
        populate_by_name=True
        json_schema_extra = {
            "example": {
                "full_name": "Simone Pecora",
                "email": "simonepecora@live.it",
                "password": "mypassword"
            }
        }