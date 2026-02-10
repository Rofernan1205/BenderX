
from decimal import Decimal
from app.models import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List, TYPE_CHECKING, Optional
from sqlalchemy import Text, Numeric, ForeignKey, true

if TYPE_CHECKING:
    from .products import Product
    from .users import User




class PriceHistory(Base):
    __tablename__ = "price_histories"
    old_price : Mapped[Decimal] = mapped_column(Numeric(10,2), nullable=False)
    new_price : Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    reason : Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    user_id : Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    product_id : Mapped[int] = mapped_column(ForeignKey('products.id'), nullable=False, ondelete='RESTRICT')

    products : Mapped[List["Product"]] = relationship(back_populates="price_history")
    user : Mapped["User"] = relationship(back_populates="price_histories")

    def __repr__(self) -> str:
        return f"< {self.old_price}, {self.new_price}>"











