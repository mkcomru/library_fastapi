from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional, List
from orders import OrderRead


class ClientBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    address: str

    @field_validator('phone')
    def phone_must_be_digits_and_length_10(cls, v):
        if not v.isdigit():
            raise ValueError('Phone must contain only digits')
        if len(v) != 10:
            raise ValueError('Phone must be exactly 10 digits long')
        return v


class ClientRead(BaseModel):
    id: int
    orders: Optional[List["OrderRead"]] = []

    class Config:
        orm_mode = True


class ClientCreate(ClientBase):
    pass


class ClientUpdate(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    address: str









