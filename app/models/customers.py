from app.models import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import String, Integer, Text
from typing import Optional, TYPE_CHECKING, List


class Customer(Base):
    __tablename__ = 'customers'
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(String(150), nullable=False)
    dni: Mapped[str] = mapped_column(String(8), nullable=False, unique=True, index=True)
    ruc: Mapped[str] = mapped_column(String(20), nullable=False, unique=True, index=True)
    address: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    sales: Mapped[List["Sale"]] = relationship(back_populates="customer")



    def __repr__(self) -> str:
        return f"<Customer {self.name}, {self.dni}>"

