from typing import List
from sqlalchemy.orm import Session
from pydantic import ValidationError as PydanticError
from app.repositories.payment_method_repository import PaymentMethodRepository
from app.core.exceptions import ValidationError, NotFoundError
from app.schemas.payment_method_schema import PaymentMethodCreate, PaymentMethodUpdate, PaymentMethodResponse


class PaymentMethodService:
    def __init__(self, db: Session):
        self._db = db
        self._rep = PaymentMethodRepository(db)

    def create_payment_method(self, payment_method_data: dict) -> PaymentMethodResponse:
        try:
            validated_data = PaymentMethodCreate(**payment_method_data)  # Pydantic espera recibir key = "value"
            if self._rep.get_by_code(validated_data.code):
                raise ValidationError(F"El metodo de pago {validated_data.code} ya existe")

            # Preparar datos para la db model a dict
            db_data = validated_data.model_dump()

            new_pyment_method = self._rep.create(db_data)
            return PaymentMethodResponse.model_validate(new_pyment_method)

        except PydanticError as e:
            raise ValidationError.from_pydantic(e)

    def update_payment_method(self, pay_meth_id: int, payment_method_data: dict) -> PaymentMethodResponse:
        try:
            validated_data = PaymentMethodUpdate(**payment_method_data)
            payment_method_obj = self._rep.get_by_id(pay_meth_id)
            if not payment_method_obj :
                raise NotFoundError(f"Metodo de pago {pay_meth_id} no existe existe")

            # Preparar datos para la db model a dict
            clean_update_data = validated_data.model_dump(exclude_unset=True)
            if not clean_update_data:
                raise ValidationError("No se enviaron datos válidos para actualizar.")
            updated_pyment_method = self._rep.update(payment_method_obj, clean_update_data)
            return PaymentMethodResponse.model_validate(updated_pyment_method)

        except PydanticError as e:
            raise ValidationError.from_pydantic(e)

    def get_payment_methods(self, payment_method_id: int) -> PaymentMethodResponse:
        payment_method_obj = self._rep.get_by_id(payment_method_id)
        return PaymentMethodResponse.model_validate(payment_method_obj)

    def get_all_payment_methods(self, page:int = 1, limit : int = 20) -> List[PaymentMethodResponse]:
        payment_methods = self._rep.get_all(page, limit)
        return [PaymentMethodResponse.model_validate(payment_method) for payment_method in payment_methods]

    def delete_payment_method(self, payment_method_id: int) -> None:
        payment_method_obj = self._rep.get_by_id(payment_method_id)
        if not payment_method_obj:
            raise NotFoundError(f"Metodo de pago {payment_method_id} no existe")
        self._rep.delete(payment_method_obj)








