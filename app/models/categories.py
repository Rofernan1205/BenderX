from typing import List, TYPE_CHECKING
from sqlalchemy import  String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

if TYPE_CHECKING:
    from .products import  Product



class Category(Base):
    __tablename__ = "categories"
    name : Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description : Mapped[str | None] = mapped_column(Text, nullable=True)
    # Relationship
    products : Mapped[List["Product"]] = relationship( back_populates="category", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Category {self.name}, {self.description}>"
