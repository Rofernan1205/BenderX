from decimal import Decimal

from app.models import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import String, Text, Integer, Numeric
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .users import  User
    from .products import Product

class InventoryMovement(Base):
    __tablename__ = "inventory_movements"
    movement_type : Mapped[str] =  mapped_column(String(35), nullable=False) # SALE, PURCHASE, ADJUSTMENT
    quantity : Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    stock_before: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    stock_after: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)


