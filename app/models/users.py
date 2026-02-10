from datetime import datetime
from app.models import Base
from typing import List, TYPE_CHECKING, Optional
from sqlalchemy import String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column


if TYPE_CHECKING:
    from .roles import Role
    from .branches import Branch
    # from .auditLog import AuditLog
    # from .sales import  Sale
    from .purchases import Purchase
    from .cashRegisters import CashRegister
    from .inventoryMovements import InventoryMovement
    from .priceHistory import  PriceHistory
    from .userSessions import UserSession
    from cashSessions import  CashSession



class User(Base):
    __tablename__ = "users"
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    last_name: Mapped[str] = mapped_column(String(80), nullable=False)
    username: Mapped[str] = mapped_column(String(25), nullable=False, unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(15),nullable=False)
    address: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    last_login: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

    role_id:Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False)
    branch_id :Mapped[int] = mapped_column(ForeignKey('branches.id'), nullable=False)

    role: Mapped["Role"] = relationship(back_populates="users")
    branch: Mapped["Branch"] = relationship(back_populates="users")
    # logs :Mapped[List["AuditLog"]] = relationship(back_populates="user")
    # sales:Mapped[List[Sale]] = relationship(back_populates="user")
    purchases:Mapped[List[Purchase]] = relationship(back_populates="user")
    cashRegisters:Mapped[List[CashRegister]] = relationship()
    inventoryMovements:Mapped[List[InventoryMovement]] = relationship(back_populates="user")
    price_histories : Mapped[List[PriceHistory]] = relationship(back_populates="user")
    user_sessions:Mapped[List[UserSession]] = relationship(back_populates="user", cascade="all, delete-orphan")
    cash_registers: Mapped[List[CashRegister]] = relationship(back_populates="user")






    def __repr__(self) -> str:
        return f"<Users {self.name}, {self.last_name}, {self.username} >"



