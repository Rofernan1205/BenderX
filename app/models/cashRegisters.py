from app.models import Base
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .cashSessions import CashSession



class CashRegister(Base):
    __tablename__ = "cash_registers"


