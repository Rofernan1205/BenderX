from typing import List
from sqlalchemy.orm import Session
from pydantic import ValidationError as PydanticError
from app.repositories.cash_register_repository import CashRegisterRepository
from app.core.exceptions import ValidationError, NotFoundError
from app.schemas.cash_register_schema import CashRegisterCreate, CashRegisterUpdate, CashRegisterResponse

class CashRegisterService:
    def __init__(self, db: Session):
        self._db = db
        self._rep = CashRegisterRepository(db)

    def create_cash_register(self, cash_register :dict ) -> CashRegisterResponse:
        try:
            # 1. Validar datos con Pydantic
            validated_data = CashRegisterCreate(**cash_register)
            if self._rep.get_by_name(validated_data.name):
                raise ValidationError(f'La caja {validated_data.name} ya existe')

            # 3. Preparar datos para la DB
            db_data = validated_data.model_dump()

            new_cash_register = self._rep.create(db_data)
            return CashRegisterResponse.model_validate(new_cash_register)
        except PydanticError as e:
            raise ValidationError.from_pydantic(e)


    def update_cash_register(self,cash_register_id : int,  cash_register :dict ) -> CashRegisterResponse:
        try:
            # 1. Validar datos con Pydantic
            validated_data = CashRegisterUpdate(**cash_register)
            cash_register_obj = self._rep.get_by_id(cash_register_id)
            if not cash_register_obj:
                raise NotFoundError(f'La caja {validated_data.name} no existe')

            # 3. Detectar cambios reales (exclude_unset)
            clean_update_data = validated_data.model_dump(exclude_unset=True)

            if not clean_update_data:
                raise ValidationError("No se enviaron datos válidos para actualizar.")

            update_cash_register_obj = self._rep.update(cash_register_obj, clean_update_data)

            return CashRegisterResponse.model_validate(update_cash_register_obj)
        except PydanticError as e:
            raise ValidationError.from_pydantic(e)


    def get_cash_register(self, cash_register_id : int) -> CashRegisterResponse:
        cash_register_obj =  self._rep.get_by_id(cash_register_id)
        if not cash_register_obj:
            raise NotFoundError(f'La caja {cash_register_id} no existe')
        return CashRegisterResponse.model_validate(cash_register_obj)


    def get_all_cash_registers(self, page : int = 1, limit : int = 20) -> List[CashRegisterResponse]:
        cash_registers = self._rep.get_all(page=page, limit=limit)
        return [CashRegisterResponse.model_validate(cash_register) for cash_register in cash_registers]

    def delete_cash_register(self, cash_register_id : int) -> None:
        cash_register = self._rep.get_by_id(cash_register_id)
        if not cash_register:
            raise NotFoundError(f'La caja {cash_register_id} no existe')
        if cash_register.id == 1:
            raise ValidationError('La caja 1 no se puede eliminar')
        self._rep.delete(cash_register)



