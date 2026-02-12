from decimal import Decimal

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Numeric
from app.models.base import Base
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .cashSessions import CashSession
    from .paymentMethods import PaymentMethod




class SalePayment(Base):
    __tablename__ = "sale_payments"

    sale_id: Mapped[int] = mapped_column(ForeignKey("sales.id" , ondelete="CASCADE"), nullable=False)
    payment_method_id : Mapped[int] = mapped_column(ForeignKey("payment_methods.id"), nullable=False)
    cash_session_id : Mapped[int] = mapped_column(ForeignKey("cash_sessions.id"), nullable=False)


    amount : Mapped[Decimal] = mapped_column(Numeric(18,2)) # Monto o cantidad
    reference : Mapped[Optional[str]] = mapped_column(String(100), nullable=True, index=True) # Numero de operacion
    status : Mapped[str] = mapped_column(String(50), default="completed") # Completado, pendiente, cancelado

    sale: Mapped["Sale"] = relationship(back_populates="sale_payments")
    payment_method: Mapped["PaymentMethod"] = relationship( back_populates="sale_payments")
    cash_session: Mapped["CashSession"] = relationship(back_populates="sale_payments")


    def __repr__(self) -> str:
        return f"<SalePayment: {self.reference}>"



