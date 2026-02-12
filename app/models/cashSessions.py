from datetime import datetime
from decimal import Decimal
from app.models.base import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey, String, Numeric, Text
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .users import  User
    from .cashRegisters import  CashRegister
    from .userSessions import UserSession
    from .sales import Sale
    from .salePayments import SalePayment
    # from .auditLog import AuditLog
    from .cashMovements import CashMovement



class CashSession(Base):
    __tablename__ = 'cash_sessions'
    # fecha apertura

    opening_balance: Mapped[Decimal] = mapped_column(Numeric(18,2), nullable=False) # Balance inicial
    closing_balance: Mapped[Decimal] = mapped_column(Numeric(18,2)) # Balance final
    difference_amount: Mapped[Decimal] = mapped_column(Numeric(18,2)) # Diferencia
    status: Mapped[Optional[str]] = mapped_column(String(20), default="OPEN")
    notes : Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    exited_at: Mapped[Optional[datetime]] = mapped_column(null=True)

    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"))
    cash_register_id : Mapped[int] = mapped_column(ForeignKey("cash_registers.id"))
    user_session_id : Mapped[int] = mapped_column(ForeignKey("user_sessions.id"))

    user: Mapped["User"] = relationship(back_populates="cash_sessions")
    cash_register: Mapped["CashRegister"] = relationship(back_populates="cash_sessions")
    user_session: Mapped["UserSession"] = relationship(back_populates="user_sessions")

    cash_movements : Mapped[List["CashMovement"]] = relationship(back_populates="cash_session", cascade="all, delete-orphan")
    sales: Mapped[List["Sale"]] = relationship(back_populates="cash_session")
    sale_payments: Mapped[List["SalePayment"]] = relationship(back_populates="cash_session")
    # logs: Mapped[list["AuditLog"]] = relationship(back_populates="cash_session")







