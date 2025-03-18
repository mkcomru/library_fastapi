from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, int_primary_key
from app.models.authors import Authors
from app.models.orders import Orders
import enum


class Genre(enum.Enum):
    fantasy = "fantasy"
    science_fiction = "science_fiction"
    mystery = "mystery"
    romance = "romance"
    horror = "horror"
    thriller = "thriller"
    biography = "biography"
    autobiography = "autobiography"


class Books(Base):
    __tablename__ = "books"

    id: Mapped[int_primary_key]
    title: Mapped[str] = mapped_column(String(100))
    year: Mapped[int]
    genre: Mapped[Genre]
    rating: Mapped[float]
    publisher: Mapped[str] = mapped_column(String(100))
    pages: Mapped[int]
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id", ondelete="CASCADE"))
    author: Mapped["Authors"] = relationship("Authors", back_populates="books")
    orders: Mapped[list["Orders"]] = relationship("Orders", back_populates="book")