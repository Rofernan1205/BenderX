from datetime import datetime
from decimal import Decimal

from app.models import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, String, Numeric, Text
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .users import  User
    from .cashRegisters import  CashRegister
    from .userSessions import UserSession
    from .sales import Sale
    from .salePayments import SalePayment
    from .auditLog import AuditLog


class CashSession(Base):
    __tablename__ = 'cash_sessions'
    # fecha apertura
    exited_at: Mapped[Optional[datetime]] = mapped_column(null=True)
    opening_balance: Mapped[Decimal] = mapped_column(Numeric(10,2), nullable=False) # Balance inicial
    closing_balance: Mapped[Decimal] = mapped_column(Numeric(10,2)) # Balance final
    difference_amount: Mapped[Decimal] = mapped_column(Numeric(10,2)) # Diferencia
    status: Mapped[Optional[str]] = mapped_column(String(20), default="OPEN")
    notes : Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"))
    cash_register_id : Mapped[int] = mapped_column(ForeignKey("cash_registers.id"))
    user_session_id : Mapped[int] = mapped_column(ForeignKey("user_sessions.id"))

    user: Mapped["User"] = relationship(back_populates="cash_registers")
    cash_register: Mapped["CashRegister"] = relationship(back_populates="cash_registers")
    user_session: Mapped["UserSession"] = relationship(back_populates="user_sessions")

    sales: Mapped[List["Sale"]] = relationship(back_populates="cash_register")
    sale_payments: Mapped[List["SalePayment"]] = relationship(back_populates="cash_register")
    logs: Mapped[list["AuditLog"]] = relationship(back_populates="cash_register")






