
from decimal import Decimal
from app.models.base import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List, TYPE_CHECKING, Optional
from sqlalchemy import Text, Numeric, ForeignKey

if TYPE_CHECKING:
    from .products import Product
    from .users import User




class PriceHistory(Base):
    __tablename__ = "price_histories"
    old_price : Mapped[Decimal] = mapped_column(Numeric(18,2), nullable=False)
    new_price : Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    reason : Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    user_id : Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    product_id : Mapped[int] = mapped_column(ForeignKey('products.id' , ondelete='RESTRICT'), nullable=False)

    product : Mapped[List["Product"]] = relationship("Product", back_populates="price_histories")
    user : Mapped["User"] = relationship("User", back_populates="price_histories")

    def __repr__(self) -> str:
        return f"< {self.old_price}, {self.new_price}>"











