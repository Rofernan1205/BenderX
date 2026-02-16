from decimal import Decimal
from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import  TYPE_CHECKING
from app.models.base import Base
if TYPE_CHECKING:
    from .users import User
    from .branches import Branch
    from .cashSessions import CashSession


class CashMovement(Base):
    __tablename__ = 'cash_movements'

    amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    type: Mapped[str] = mapped_column(String(20))  # "INGRESO" o "EGRESO"
    reason: Mapped[str] = mapped_column(String(255))  # Ej: "Pago de delivery", "Aporte de sencillo"
    cash_session_id: Mapped[int] = mapped_column(
        ForeignKey("cash_sessions.id", ondelete="CASCADE"),
        index=True
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    branch_id: Mapped[int] = mapped_column(ForeignKey("branches.id"))

    cash_session: Mapped["CashSession"] = relationship("CashSession", back_populates="cash_movements")
    user: Mapped["User"] = relationship("User")
    branch: Mapped["Branch"] = relationship("Branch")

    def __repr__(self) -> str:
        return f"<CashMovement: {self.amount}>"