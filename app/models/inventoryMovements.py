from decimal import Decimal

from app.models import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import String, Text, Numeric, ForeignKey
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .users import  User
    from .products import Product

class InventoryMovement(Base):
    __tablename__ = "inventory_movements"
    movement_type : Mapped[str] =  mapped_column(String(35), nullable=False) # SALE, PURCHASE, ADJUSTMENT
    quantity : Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    stock_before: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    stock_after: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    reason: Mapped[Optional[str]] = mapped_column(Text, nullable=False)

    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    product_id : Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)

    user :Mapped["User"] = relationship(back_populates="inventory_movements")
    product :Mapped["Product"] = relationship(back_populates="inventory_movements")

    def __repr__(self) -> str:
        return f"<Movement {self.movement_type}>"


