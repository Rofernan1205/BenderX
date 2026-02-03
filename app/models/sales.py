from app.models import Base
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from .cashSessions import CashSession

class Sale(Base):
    __tablename__ = "sales"