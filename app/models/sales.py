from sqlalchemy.orm import Mapped, relationship

from app.models import Base
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from .cashSessions import CashSession
    from .salePayments import SalePayment

class Sale(Base):
    __tablename__ = "sales"
    sale_payments : Mapped[List["SalePayment"]] = relationship(back_populates="sale", cascade="all, delete-orphan")
