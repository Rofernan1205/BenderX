from typing import List
from sqlalchemy.orm import Session
from pydantic import ValidationError as PydanticError
from app.repositories.tax_repository import TaxRepository
from app.core.exceptions import ValidationError, NotFoundError
from app.schemas.tax_schema import  TaxCreate, TaxUpdate, TaxResponse

class TaxService:
    def __init__(self, db: Session):
        self._db = db
        self._rep = TaxRepository(db)

    def create_tax(self, tax_data: dict) -> TaxResponse:
        try:
            validated_data = TaxCreate(**tax_data) # Pydantic espera recibir kay = "value"
            if self._rep.get_by_code(validated_data.code):
                raise ValidationError(F"El impuesto {validated_data.code} ya existe")
            # Preparar datos para la DB
            db_data = validated_data.model_dump()
            new_tax_obj = self._rep.create(db_data)
            return TaxResponse.model_validate(new_tax_obj)

        except PydanticError as e:
            raise ValidationError.from_pydantic(e)


    def update_tax(self, tax_id: int, tax_data: dict) -> TaxResponse:
        try:
            validated_data = TaxUpdate(**tax_data)

            tax_obj = self._rep.get_by_id(tax_id)

            if not tax_obj :
                raise NotFoundError(F"El impuesto {validated_data.id} no existe")
            # Detectar cambios cambios
            clean_update_data = validated_data.model_dump(exclude_unset=True)
            if not clean_update_data:
                raise ValidationError("No se enviaron datos válidos para actualizar.")

            update_tax_obj = self._rep.update(tax_obj, clean_update_data)
            return TaxResponse.model_validate(update_tax_obj)

        except PydanticError as e:
            raise ValidationError.from_pydantic(e)

    def get_tax(self, tax_id: int) -> TaxResponse:
        tax_obj = self._rep.get_by_id(tax_id)
        if not tax_obj:
            raise NotFoundError(F"El impuesto {tax_id} no existe")
        return TaxResponse.model_validate(tax_obj)


    def get_all_taxes(self, page:int = 1, limit : int = 20) -> List[TaxResponse]:
        taxes = self._rep.get_all(page, limit)
        return [TaxResponse.model_validate(tax) for tax in taxes]



    def delete_tax(self, tax_id: int) -> None:
        tax_obj = self._rep.get_by_id(tax_id)
        if not tax_obj:
            raise NotFoundError(F"El impuesto {tax_id} no existe")
        self._rep.delete(tax_obj)

