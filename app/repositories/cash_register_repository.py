from typing import Optional

from sqlalchemy.orm import Session
from app.models.cashRegisters import CashRegister
from app.repositories.base_repository import BaseRepository

class CashRegisterRepository(BaseRepository[CashRegister]):
    def __init__(self, db: Session):
        super().__init__(db, CashRegister)

    def get_by_name(self, name: str) -> Optional[CashRegister]:
        cash_register_obj = self._db.query(CashRegister).filter(CashRegister.name == name).first()
        return cash_register_obj


