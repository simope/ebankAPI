from pydantic import BaseModel, ConfigDict, field_validator

allowed = ['EUR', 'USD', 'GBP']
class TransferBase(BaseModel):
    id: int
    sender_id: int
    recipient_id: int
    currency: str
    amount: float

    model_config = ConfigDict(from_attributes=True)

    @field_validator('currency')
    @classmethod
    def currency_is_allowed(cls, curr: str) -> str:
        if curr not in allowed:
            raise ValueError('use a supported currency! You used '+curr)
        return curr

class CreateTransfer(TransferBase):
    model_config = ConfigDict(from_attributes=True)