from app.models.base import Base
from sqlalchemy.orm import   Mapped, mapped_column
from sqlalchemy import String, Text
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    pass
    # from .sales import Sale


class Customer(Base):
    __tablename__ = 'customers'
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(String(150), nullable=False)
    dni: Mapped[str] = mapped_column(String(8), nullable=False, unique=True, index=True)
    ruc: Mapped[str] = mapped_column(String(20), nullable=False, unique=True, index=True)
    address: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # sales: Mapped[List["Sale"]] = relationship("Sale", back_populates="customer")



    def __repr__(self) -> str:
        return f"<Customer {self.name}, {self.dni}>"

