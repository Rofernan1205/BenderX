from app.models.base import Base
from sqlalchemy.orm import relationship, Mapped , mapped_column
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .products import Product
    from .taxes import Tax


class ProductTax(Base):
    __tablename__ = "product_taxes"
    product_id : Mapped[int] = mapped_column(ForeignKey("products.id" , ondelete="CASCADE"))
    tax_id : Mapped[int] = mapped_column(ForeignKey("taxes.id" , ondelete="CASCADE"))

    product : Mapped["Product"] = relationship("Product", back_populates="product_taxes")
    tax : Mapped["Tax"] = relationship("Tax", back_populates= "product_taxes" )