from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Text
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .users import User
    from .branches import Branch

from app.models import Base


class CashRegister(Base):
    __tablename__ = "cash_register"
    code : Mapped[str] = mapped_column(String(25), unique=True, nullable=False) # CAJA01 POS01
    name : Mapped[str] =  mapped_column(String(40), nullable=False , index=True) # Caja principal


    