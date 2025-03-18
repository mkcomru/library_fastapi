from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, int_primary_key
from app.models.orders import Orders


class Clients(Base):
    __tablename__ = "clients"

    id: Mapped[int_primary_key]
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100))
    phone: Mapped[str] = mapped_column(String(10))
    address: Mapped[str] = mapped_column(String(100))
    orders: Mapped[list["Orders"]] = relationship("Orders", back_populates="client")