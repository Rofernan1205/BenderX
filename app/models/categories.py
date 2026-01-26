from typing import List
from sqlalchemy import  String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base



class Category(Base):
    __tablename__ = "categories"
    name : Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description : Mapped[str | None] = mapped_column(String(100))
    # Relationship
    products : Mapped[List["Product"]] = relationship("Product", back_populates="category", cascade="all, delete-orphan")
