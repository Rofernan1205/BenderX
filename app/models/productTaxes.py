from app.models import Base
from sqlalchemy.orm import relationship, Mapped , mapped_column
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .products import Product
    from .taxes import Tax


class ProductTax(Base):
    __tablename__ = "product_taxes"
    product_id : Mapped[int] = mapped_column(ForeignKey("products.id"), ondelete="CASCADE" , primary_key=True)
    tax_id : Mapped[int] = mapped_column(ForeignKey("taxes.id"), ondelete="CASCADE", primary_key=True)

    product : Mapped["Product"] = relationship(back_populates="product_taxes")
    tax : Mapped["Tax"] = relationship( back_populates= "product_taxes" )