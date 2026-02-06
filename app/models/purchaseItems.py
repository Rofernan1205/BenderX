from decimal import Decimal

from app.models import Base
from typing import List, TYPE_CHECKING, Optional
from sqlalchemy import String, Text, ForeignKey, Numeric, Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column

if TYPE_CHECKING:
    from .purchases import Purchase
    from .products import Product

class PurchaseItem(Base):
    __tablename__ = "purchase_items"

    quantity: Mapped[int] = mapped_column(Integer, nullable=False) # Cantidad comprada
    unit_cost: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False) # Costo unitario
    # Subtotal del item (quantity * unit_cost)
    subtotal: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id", ondelete="RESTRICT"), nullable=False)
    purchase_id: Mapped[int] = mapped_column(ForeignKey("purchases.id", ondelete="CASCADE"), nullable=False)

    purchase: Mapped["Purchase"] = relationship(back_populates="purchase_items")
    product: Mapped["Product"] = relationship()

    def __repr__(self) -> str:
        return F"< PurchaseItem product_id : {self.product_id} >"


