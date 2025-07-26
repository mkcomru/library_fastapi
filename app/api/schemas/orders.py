from pydantic import BaseModel
from datetime import date
from typing import Optional
import enum


class BorrowingStatus(str, enum.Enum):
    active = "active"
    returned = "returned"
    overdue = "overdue"


class OrderRead(BaseModel):
    id: int
    order_date: date
    return_date: Optional[date] = None
    borrowing_status: BorrowingStatus

    class Config:
        orm_mode = True


class OrderCreate(BaseModel):
    client_id: int
    book_id: int
    order_date: date
    return_date: Optional[date] = None
    borrowing_status: BorrowingStatus















