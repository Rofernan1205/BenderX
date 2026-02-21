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

    def create_branch(self, branch_data: dict) -> Branch:
        try:
            # 1. Validar datos
            validated_data = BranchCreate(**branch_data)

            # 2. Lógica de negocio
            if self._repo.get_by_name(validated_data.name):
                raise ValidationError(f"La sucursal '{validated_data.name}' ya existe.")

            # 3. Persistencia
            new_branch = self._repo.create(validated_data.model_dump())
            return new_branch

        except PydanticError as e:
            # Llamamos al manejador que lanza la excepción
            ValidationError.from_pydantic(e)


    def update_branch(self, branch_id: int, branch_data: dict) -> Branch:
        try:
            validated_data = BranchUpdate(**branch_data)

            branch_obj = self._repo.get_by_id(branch_id)
            if not branch_obj:
                raise NotFoundError("Sucursal no existe")

            clean_update_data = validated_data.model_dump(exclude_unset=True)

            if not clean_update_data:
                raise ValidationError("No se enviaron datos válidos para actualizar.")

            updated_branch = self._repo.update(branch_obj, clean_update_data)
            return updated_branch

        except PydanticError as e:
            ValidationError.from_pydantic(e)



    def get_branch(self, branch_id: int) -> Branch | None:
        return self._repo.get_by_id(branch_id)

    def get_all_branches(self, page: int = 1, limit: int = 20):
        return self._repo.get_all(page=page, limit=limit)

    def delete_branch(self, branch_id: int) -> None:
        if branch_id == 1:
            raise ValidationError("No se puede eliminar la sucursal principal")

        branch_obj = self._repo.get_by_id(branch_id)
        if not branch_obj:
            raise NotFoundError("Sucursal no existe")

        self._repo.delete(branch_obj)
        self._db.commit()  # IMPORTANTE: el delete también necesita commit



