from sqlalchemy.orm import Session
from app.core.exceptions import ValidationError, NotFoundError
from app.models import Branch
from app.repositories.branch_repository import BranchRepository

from app.schemas.branch_schema import BranchCreate, BranchUpdate
from pydantic import ValidationError as PydanticError


class BranchService:
    def __init__(self, db: Session) -> None:
        self._db = db
        self._repo = BranchRepository(db)

    def create_branch(self, branch_data: dict) -> Branch :
        try:
            # 1. Validar datos para creación
            validated_data = BranchCreate(**branch_data)

            # 2. Verificar si sucursal ya existe
            if self._repo.get_by_name(validated_data.name):
                raise ValidationError(f"La sucursal '{validated_data.name}' ya existe.")

            return self._repo.create(validated_data.model_dump()) # Model_dump convierte obj a dict

        except PydanticError as e:
            self._handle_pydantic_errors(e)

    def update_branch(self, branch_id: int, branch_data: dict) -> Branch | None:
        try:
            # 1. Validar datos para actualización
            validated_data = BranchUpdate(**branch_data)

            # 2. Buscar objeto existente
            branch_obj = self._repo.get_by_id(branch_id)
            if not branch_obj:
                raise NotFoundError("Sucursal no existe")

            # 3. exclude_unset=True: Pydantic solo incluye en el diccionario los campos que el usuario realmente escribió en el formulario.
            clean_update_data = validated_data.model_dump(exclude_unset=True) # Model_dump convierte obj a dict

            if not clean_update_data:
                raise ValidationError("No se enviaron datos válidos para actualizar.")

            # 4. Actualizar dinámicamente el objeto
            for key, value in clean_update_data.items():
                setattr(branch_obj, key, value)

            return self._repo.update(branch_obj)

        except PydanticError as e:
            self._handle_pydantic_errors(e)


    def _handle_pydantic_errors(self, e: PydanticError):
        """Traduce errores de Pydantic a tus excepciones de BenderX"""
        error_detail = e.errors()[0]
        campo = error_detail['loc'][0]
        mensaje = error_detail['msg']
        raise ValidationError(f"Error en {campo}: {mensaje}")

    # --- Los demás métodos se mantienen igual ---
    def get_branch(self, branch_id: int) -> Branch | None:
        return self._repo.get_by_id(branch_id)

    def get_all_branches(self, page: int = 1, limit: int = 20):
        return self._repo.get_all(page=page, limit=limit)

    def delete_branch(self, branch_id: int) -> None:
        branch_obj = self._repo.get_by_id(branch_id)
        if not branch_obj:
            raise NotFoundError("Sucursal no existe")
        # Corrección: si id es int, comparar con 1 es suficiente
        if branch_id == 1:
            raise ValidationError("No se puede eliminar la sucursal principal del sistema")



