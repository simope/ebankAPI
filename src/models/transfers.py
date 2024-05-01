from uuid import uuid4, UUID
from pydantic import ConfigDict, BaseModel, Field, field_validator

allowed_currencies = ['EUR', 'GBP', 'USD']

class Transfer(BaseModel):
    id: UUID = Field(default_factory=uuid4, alias="_id")
    sender_id: str
    recipient_id: str
    currency: str
    amount: float
    model_config = ConfigDict(populate_by_name=True, json_schema_extra={
        "example": {
            "sender_id": "a050f695-9b4d-4b85-95bc-efc79c394f0e",
            "recipient_id": "9098ed75-a320-4964-8bbe-b49e27fe3256",
            "currency": "EUR",
            "amount": 30.5
        }
    })

    @field_validator('currency')
    def allowed_currency(cls, currency):
        assert currency in allowed_currencies, f'must be an allowed currency, was {currency}'
        return currency