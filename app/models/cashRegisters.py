from app.models.base import Base
from typing import List, TYPE_CHECKING
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import String, ForeignKey

if TYPE_CHECKING:
    from .cashSessions import CashSession
    from .users import User
    from .branches import Branch
    # from  .userSessions import UserSession




class CashRegister(Base):
    __tablename__ = "cash_registers"
    name: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    device_code: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    user_id : Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="RESTRICT"))
    branch_id : Mapped[int] = mapped_column(ForeignKey("branches.id", ondelete="SET NULL"))

    cash_sessions : Mapped[List["CashSession"]] = relationship(back_populates="cash_register")
    branch: Mapped["Branch"] = relationship(back_populates="cash_registers")
    user: Mapped["User"] = relationship(back_populates="cash_registers")
    # user_session: Mapped["UserSession"] = relationship(back_populates="cash_registers")

    def __repr__(self) -> str:
        return f"<CashRegister: {self.name}>"












