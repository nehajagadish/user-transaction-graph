from pydantic import BaseModel


class User(BaseModel):
    user_id: str
    name: str
    email: str
    phone: str
    address: str
    payment_method: str


class Transaction(BaseModel):
    transaction_id: str
    sender: str
    receiver: str
    amount: float
    ip_address: str
    device_id: str