from decimal import Decimal
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Numeric
from typing import List, TYPE_CHECKING
from app.models import Base
if TYPE_CHECKING:
    from .productTaxes import ProductTax


class Tax(Base):
    __tablename__ = "taxes"
    code: Mapped[str] = mapped_column(String(20), nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    rate : Mapped[Decimal] = mapped_column(Numeric(10,2), nullable=False) # porcentaje
    is_percentage : Mapped[bool] = mapped_column(nullable=False, default=True)

    product_taxes : Mapped[List["ProductTax"]] = relationship(back_populates="tax", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Tax code: {self.code} name: {self.name}>"

