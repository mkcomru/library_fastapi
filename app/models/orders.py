from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.clients import Clients
from app.models.books import Books
from app.models.base import Base, int_primary_key
from datetime import date
import enum


class BorrowingStatus(enum.Enum):
    active = "active"
    returned = "returned"
    overdue = "overdue"


class Orders(Base):
    __tablename__ = "orders"

    id: Mapped[int_primary_key]
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id", ondelete="CASCADE"))
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id", ondelete="CASCADE"))
    order_date: Mapped[date]
    return_date: Mapped[date] = mapped_column(nullable=True)
    borrowing_status: Mapped[BorrowingStatus]
    client: Mapped["Clients"] = relationship("Clients", back_populates="orders")
    book: Mapped["Books"] = relationship("Books", back_populates="orders")

