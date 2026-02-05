from decimal import Decimal

from sqlalchemy import ForeignKey, String, Numeric, Text
from sqlalchemy.orm import Mapped, relationship, mapped_column
from app.models import Base
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:

    from .users import User
    from .cashSessions import CashSession
    from customers import Customer
    from .salePayments import SalePayment
    from .invoices import Invoice
    from .saleItems import SaleItem

class Sale(Base):
    __tablename__ = "sales"

    # Número de ticket o factura (Ej: 'TK-0001')
    invoice_number: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)

    subtotal: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)  # Sin impuestos
    tax_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=0.00)  # Total impuestos (IVA/IGV)
    discount_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=0.00)  # Descuento total
    total_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)  # Neto a pagar

    # Estado de la venta: 'completed' (pagada), 'pending' (crédito), 'cancelled' (anulada)
    status: Mapped[str] = mapped_column(String(20), default="completed", index=True)

    # Notas adicionales
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)


    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), ondelete="RESTRICT")
    customer_id: Mapped[Optional[int]] = mapped_column(ForeignKey("customers.id", ondelete="SET NULL"), nullable=True)
    cash_session_id : Mapped[int] = mapped_column(ForeignKey("cash_sessions.id"), ondelete="RESTRICT")

    user: Mapped["User"] = relationship(back_populates="sales")
    customer: Mapped["Customer"] = relationship(back_populates="sales")
    cash_session: Mapped["CashSession"] = relationship(back_populates="sales")

    invoice: Mapped["Invoice"] = relationship(back_populates="sale")
    sale_payments : Mapped[List["SalePayment"]] = relationship(back_populates="sale", cascade="all, delete-orphan")
    sale_items : Mapped[List["SaleItem"]] = relationship(back_populates="sale", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Sale {self.invoice_number}>"



