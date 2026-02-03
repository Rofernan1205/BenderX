from app.models import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .cashSessions import CashSession


class SalePayment(Base):
    __tablename__ = "sale_payments"