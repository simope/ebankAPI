from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

allowed_currencies = ['EUR', 'GBP', 'USD']

class Transfer(Base):
    __tablename__ = "transfers"
    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey("users.id"))
    recipient_id = Column(Integer, ForeignKey("users.id"))
    currency = Column(String)
    amount = Column(Float)

    sender = relationship("User", backref="sender_users", foreign_keys=[sender_id])
    recipient = relationship("User", backref="recipient_users", foreign_keys=[recipient_id])