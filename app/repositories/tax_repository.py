from sqlalchemy.orm import Session
from app.models.taxes import  Tax
from typing import Optional
from app.repositories.base_repository import BaseRepository

class TaxRepository(BaseRepository[Tax]):
    def __init__(self, db : Session):
        super().__init__(db, Tax)

    def get_by_code(self, code: str) -> Optional[Tax]:
        return self._db.query(Tax).filter(Tax.code == code).first()

    def get_by_name(self, name: str) -> Optional[Tax]:
        return self._db.query(Tax).filter(Tax.name == name).first()






