from app.models.base import Base, int_primary_key
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from typing import Optional
from app.models.books import Books


class Authors(Base):
    __tablename__ = "authors"

    id: Mapped[int_primary_key]
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    birth_date: Mapped[date]
    death_date: Mapped[Optional[date]] 
    books: Mapped[list["Books"]] = relationship("Books", back_populates="author")