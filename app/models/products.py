from decimal import Decimal
from typing import TYPE_CHECKING, Optional
from sqlalchemy import Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

# Esto evita errores de importación circular al usar Type Hinting
if TYPE_CHECKING:
    from .categories import Category
    # from .sucursals import Sucursal


class Product(Base):
    __tablename__ = 'products'

    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False, index=True)
    brand: Mapped[Optional[str]] = mapped_column(String(80), nullable=True)
    barcode: Mapped[Optional[str]] = mapped_column(String(50), unique=True, nullable=True)
    description: Mapped[Optional[str]] = mapped_column(String(250), nullable=True)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=Decimal('0.00'))
    cost: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=Decimal('0.00'))
    stock: Mapped[int] = mapped_column(default=0, nullable=False)
    image_path: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    # ForeignKeys (Corregido: ondelete va dentro de ForeignKey)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    sucursal_id: Mapped[int] = mapped_column(ForeignKey('sucursal.id'), nullable=False)

    # Relationship (Corregido: Aquí NO es List, y el cascade va en el PADRE, no aquí)
    category: Mapped["Category"] = relationship("Category", back_populates="products")
    sucursal: Mapped["Sucursal"] = relationship("Sucursal", back_populates="products")



