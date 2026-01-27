from sqlalchemy import ForeignKey, String, Numeric, Text
from typing import Optional, TYPE_CHECKING
from app.models import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from decimal import Decimal

if TYPE_CHECKING:
    pass
    # from .sale import Sale  # Asumiendo tus nombres de archivo
    from .paymentMethods import PaymentMethod


class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)


    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False) # Monto sin comisiones
    fee_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=Decimal('0.00')) #Comisiones credit card 4.5%
    total_paid: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False) # Monto total

    # Referencia de transacción (ej. número de operación de la tarjeta)
    reference_number: Mapped[str | None] = mapped_column(String(100), nullable=True)

    sale_id: Mapped[int] = mapped_column(ForeignKey("sales.id", ondelete="RESTRICT"), nullable=False)
    payment_method_id: Mapped[int] = mapped_column(ForeignKey("payment_methods.id", ondelete="RESTRICT"),nullable=False)

    # RELACIONES
    sale: Mapped["Sale"] = relationship(back_populates="payments")
    payment_method: Mapped["PaymentMethod"] = relationship(back_populates="payments")

    def __repr__(self):
        return f"<Payment(id={self.id}, total={self.total_paid}, ref={self.reference_number})>"



