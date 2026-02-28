from sqlalchemy.orm import Session
from app.models.paymentMethods import PaymentMethod
from typing import Optional
from app.repositories.base_repository import BaseRepository

class PaymentMethodRepository(BaseRepository[PaymentMethod]):
    def __init__(self, db : Session):
        super().__init__(db, PaymentMethod)

    def get_by_code(self, code: str) -> Optional[PaymentMethod]:
        return self._db.query(PaymentMethod).filter(PaymentMethod.code == code).first()

    def get_by_name(self, name: str) -> Optional[PaymentMethod]:
        return self._db.query(PaymentMethod).filter(PaymentMethod.name == name).first()
