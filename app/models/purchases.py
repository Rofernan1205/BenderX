from decimal import Decimal

from app.models import Base
from typing import List, TYPE_CHECKING, Optional
from sqlalchemy import String, Text, ForeignKey, Numeric
from sqlalchemy.orm import relationship, Mapped, mapped_column

if TYPE_CHECKING:
    from .suppliers import Supplier
    from .users import User
    from purchaseItems import  PurchaseItem


class Purchase(Base):
    __tablename__ = "purchases"

    # Número de factura o remisión del proveedor (Ej: 'FAC-9928')
    reference_number: Mapped[Optional[str]] = mapped_column(String(100), index=True)

    subtotal: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False) # Monto Neto de compras sin inpuestos
    tax_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=0.00) # Impuesto aplicado al subtotal
    total_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False) # suma subtotal + impuestos

    # 'ordered' , 'received', 'cancelled'
    status: Mapped[str] = mapped_column(String(20), default="received", index=True)

    # 'paid' , 'partial' , 'pending'
    payment_status: Mapped[str] = mapped_column(String(20), default="paid")
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="RESTRICT"), nullable=False)
    supplier_id : Mapped[int] = mapped_column(ForeignKey("suppliers.id", ondelete="RESTRICT"), nullable=False)

    supplier: Mapped["Supplier"] = relationship(back_populates="purchases")
    user: Mapped["User"] = relationship(back_populates="purchases")
    purchase_items: Mapped[List["PurchaseItem"]] = relationship( back_populates="purchase", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Purchase {self.reference_number}>"




