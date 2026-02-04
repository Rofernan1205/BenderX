from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.models import Base
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from .invoices import Invoice
    from .users import User

    from .cashSessions import CashSession
    from .salePayments import SalePayment

class Sale(Base):
    __tablename__ = "sales"


    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), ondelete="RESTRICT")
    customer_id : Mapped[int] = mapped_column(ForeignKey("customers.id"), ondelete="RESTRICT")
    cash_session_id : Mapped[int] = mapped_column(ForeignKey("cash_sessions.id"), ondelete="RESTRICT")









    sale_payments : Mapped[List["SalePayment"]] = relationship(back_populates="sale", cascade="all, delete-orphan")
