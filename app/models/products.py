from decimal import Decimal
from typing import TYPE_CHECKING, Optional, List
from sqlalchemy import String, Numeric, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

if TYPE_CHECKING:
    from .categories import Category
    from .branches import  Branch
    from .inventoryMovements import InventoryMovement
    from .productTaxes import ProductTax
    from .priceHistory import PriceHistory
    # from .purchaseItems import PurchaseItem
    # from .saleItems import SaleItem


class Product(Base):
    __tablename__ = 'products'

    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False, index=True)
    brand: Mapped[Optional[str]] = mapped_column(String(80), nullable=True)
    barcode: Mapped[Optional[str]] = mapped_column(String(50), unique=True, nullable=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    price: Mapped[Decimal] = mapped_column(Numeric(18, 2), default=Decimal('0.00'))
    cost: Mapped[Decimal] = mapped_column(Numeric(18, 2), default=Decimal('0.00'))
    stock: Mapped[int] = mapped_column(default=0, nullable=False)
    image_path: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    # ForeignKeys
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    branch_id: Mapped[int] = mapped_column(ForeignKey('branches.id'), nullable=False)

    # Relationship
    category: Mapped["Category"] = relationship(back_populates="products")
    branch: Mapped["Branch"] = relationship( back_populates="products")

    price_histories: Mapped[List["PriceHistory"]] = relationship(back_populates="product")
    inventory_movements : Mapped[List["InventoryMovement"]] = relationship(back_populates="product")
    product_taxes : Mapped[List["ProductTax"]] = relationship(back_populates="product")
    # purchase_items : Mapped[List["PurchaseItem"]] = relationship(back_populates="product")
    # sale_items : Mapped[List["SaleItem"]] = relationship(back_populates="product")



    def __repr__(self) -> str:
        return f"<Product {self.name}, {self.brand}, {self.price}, {self.cost}, {self.stock}>"



