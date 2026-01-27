from app.models import Base
from typing import List, TYPE_CHECKING, Optional
from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column



class Supplier(Base):
    __tablename__ = 'suppliers'
    name : Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    ruc : Mapped[str] = mapped_column(String(20), unique=True, nullable=False , index=True)
    phone : Mapped[str] = mapped_column(String(20), nullable=False)
    email : Mapped[str] = mapped_column(String(150), nullable=False)
    address : Mapped[Optional[str]] = mapped_column(Text,nullable=True)

    shopping :Mapped[List["Shopping"]] =relationship(back_populates="supplier")

    def __repr__(self) -> str:
        return f"<Supplier {self.name}, {self.ruc}>"