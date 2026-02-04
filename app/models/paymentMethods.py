from app.models import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import String
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .salePayments import SalePayment


class PaymentMethod(Base):
    __tablename__ = "payment_methods"
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True, index=True)
    code: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)

    # Reglas de negocio
    fee_percentage: Mapped[float] = mapped_column(default=0.0) # Porcenjate de comisión se aplica  al monto de pago
    fee_fixed: Mapped[float] = mapped_column(default=0.0) # Comision fija

    requires_reference: Mapped[bool] = mapped_column(default=False) # Indica si el pago debe tener comprobante
    allows_installments: Mapped[bool] = mapped_column(default=False) # Permite pago en cuotas
    max_installments: Mapped[int | None] = mapped_column(nullable=True) # Número máximode cuotas

    # Control
    is_active: Mapped[bool] = mapped_column(default=True)

    sale_payments: Mapped[List["SalePayment"]] = relationship(back_populates="payment_method")

    def __repr__(self) -> str:
        return f"<PaymentMethod name={self.name}>"