from app.models.companyParameters import CompanyParameter
from sqlalchemy.orm import Session
from typing import Optional
from app.repositories.base_repository import BaseRepository

class CompanyParameterRepository(BaseRepository[CompanyParameter]):
    def __init__(self, db: Session):
        super().__init__(db, CompanyParameter)

    def get_main_config(self) -> Optional[CompanyParameter]:
        # Retorna el primer (y único) registro de configuración.
        return self._db.query(self._model).first()



