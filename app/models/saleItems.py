from decimal import Decimal

from app.models.base import Base
from sqlalchemy.orm import relationship, Mapped ,mapped_column
from sqlalchemy import  Numeric, Integer, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .sales import Sale
    from .products import Product

class SaleItem(Base):
    __tablename__ = "sale_items"

    quantity: Mapped[int] = mapped_column(Integer, nullable=False) # Cantidad
    unit_price: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False) # Precio unitario
    subtotal: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False) # Subtotal cantidad * precio
    discount: Mapped[Decimal] = mapped_column(Numeric(18, 2), default=0.00) # Descuento

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    sale_id : Mapped[int] = mapped_column(ForeignKey("sales.id", ondelete="CASCADE"), nullable=False)

    sale : Mapped["Sale"] = relationship(back_populates="sale_items")
    product : Mapped["Product"] = relationship()

    def __repr__(self) -> str:
        return f"<SaleItem product_id={self.product_id} qty={self.quantity}>"




