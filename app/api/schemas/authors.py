from pydantic import BaseModel
from datetime import date
from typing import Optional, List
from books import BookRead


class AuthorCreate(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    death_date: Optional[date] = None


class AuthorRead(BaseModel):
    id: int
    first_name: str
    last_name: str
    birth_date: date
    death_date: Optional[date] = None

    class Config:
        orm_mode = True


class AuthorReadWithBooks(AuthorRead):
    books: List[BookRead] = []


class AuthorUpdate(BaseModel):
    id: int
    first_name: str
    last_name: str
    birth_date: date
    death_date: date

    class Config:
        orm_mode = True









