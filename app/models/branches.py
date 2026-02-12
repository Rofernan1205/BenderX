from typing import List, TYPE_CHECKING, Optional
from sqlalchemy import  String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base

if TYPE_CHECKING:
    from .products import Product
    from .users import User
    from .cashRegisters import CashRegister
    from .userSessions import UserSession
    # from .auditLog import AuditLog
    # from .cashMovements import  CashMovement


class Branch(Base):
    __tablename__ = " "
    name : Mapped[str] = mapped_column(String(100), unique=True, index=True)
    phone : Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    email : Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    address : Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    users: Mapped[List["User"]] = relationship(back_populates="branch")
    products: Mapped[List["Product"]] = relationship(back_populates="branch")
    cash_registers : Mapped[List["CashRegister"]] = relationship(back_populates="branch")
    user_sessions: Mapped[List["UserSession"]] = relationship(back_populates="branch")
    # audit_logs: Mapped[List["AuditLog"]] = relationship(back_populates="branch")
    # cash_movements: Mapped[List["CashMovement"]] = relationship( back_populates="branch")


    def __repr__(self) -> str:
        return f"<Branch {self.name}, {self.phone} users>"




