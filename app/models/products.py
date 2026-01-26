from decimal import Decimal
from typing import TYPE_CHECKING, Optional
from sqlalchemy import String, Numeric, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

if TYPE_CHECKING:
    from .categories import Category
    from .branches import  Branch


class Product(Base):
    __tablename__ = 'products'

    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False, index=True)
    brand: Mapped[Optional[str]] = mapped_column(String(80), nullable=True)
    barcode: Mapped[Optional[str]] = mapped_column(String(50), unique=True, nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=Decimal('0.00'))
    cost: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=Decimal('0.00'))
    stock: Mapped[int] = mapped_column(default=0, nullable=False)
    image_path: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    # ForeignKeys
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    branch_id: Mapped[int] = mapped_column(ForeignKey('branches.id'), nullable=False)

    # Relationship
    category: Mapped["Category"] = relationship(back_populates="products")
    branch: Mapped["Branch"] = relationship( back_populates="products")

    def __repr__(self) -> str:
        return f"<Product {self.name}, {self.brand}, {self.price}, {self.cost}, {self.stock}>"



