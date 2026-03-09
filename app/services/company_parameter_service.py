from sqlalchemy.orm import Session
from typing import Optional
# from pydantic import ValidationError as PydanticError
from app.core.exceptions import ValidationError, NotFoundError
from app.repositories.company_parameter_repository import CompanyParameterRepository
from app.schemas.company_parameter_schema import (
CompanyParameterCreate,
CompanyParameterUpdate,
CompanyParameterResponse,
CompanyConfig
)


class CompanyParameterService:
    def __init__(self, db: Session):
        self._db = db
        self._rep = CompanyParameterRepository(db)

    def get_parameters(self) -> Optional[CompanyParameterResponse]:
        c_p_obj = self._rep.get_main_config()
        if not c_p_obj:
            raise NotFoundError("Los parámetros de la compañía no han sido configurados.")
        return CompanyParameterResponse.model_validate(c_p_obj)

    def create_parameter(self, schema: CompanyParameterCreate) -> CompanyParameterResponse:

        # Validación de negocio
        if self._rep.get_main_config():
            raise ValidationError("La configuración ya existe. Solo puedes actualizar los datos.")

        cp_data_db = schema.model_dump()

        # Serializar el objeto de configuración a String JSON
        if schema.config_json:
            cp_data_db["config_json"] = schema.config_json.model_dump_json()
        else:
            cp_data_db["config_json"] = CompanyConfig().model_dump_json()


        cp_new = self._rep.create(cp_data_db)
        return CompanyParameterResponse.model_validate(cp_new)

    def update_parameter(self, schema: CompanyParameterUpdate) -> CompanyParameterResponse:

        cp_obj = self._rep.get_main_config()  # No necesitamos ID porque es único
        if not cp_obj:
            raise NotFoundError("La configuración no existe. Debe crearla primero.")

        # Detectar cambios enviados desde la UI
        cp_update_db = schema.model_dump(exclude_unset=True)


        if "config_json" in cp_update_db and schema.config_json:
            cp_update_db["config_json"] = schema.config_json.model_dump_json()


        updated_obj = self._rep.update(cp_obj, cp_update_db)
        return CompanyParameterResponse.model_validate(updated_obj)








