from sqlalchemy.orm import Session

from app.core.exceptions import ValidationError,BranchNotFoundException
from app.models import Branch
from app.repositories.branch_repository import BranchRepository

class BranchService:
    def __init__(self, db: Session) -> None :
        self._db = db
        self._repo = BranchRepository(db)

    def create_branch(self, branch_data: dict) -> Branch | None:
        if self._repo.get_by_name(branch_data["name"]):
            raise ValidationError("Sucursal ya existe")
        branch = self._repo.create(branch_data)
        return branch

    def update_branch(self, branch_id: int, branch_data: dict) -> Branch | None:
        branch_obj = self._repo.get_by_id(branch_id)
        if not branch_obj:
            raise BranchNotFoundException("Sucursal no existe")
        for key, value in branch_data.items():
            if hasattr(branch_obj, key):
                setattr(branch_obj, key, value)
        return self._repo.update(branch_obj)

    def get_branch(self, branch_id: int) -> Branch | None:
        return self._repo.get_by_id(branch_id)

    def get_all_branches(self, page: int = 1, limit: int = 20):
        return self._repo.get_all(page=page, limit=limit)

    def delete_branch(self, branch_id: int) -> None:
        branch_obj = self._repo.get_by_id(branch_id)
        if not branch_obj:
            raise ValidationError("Sucursal no existe")
        if branch_obj.id == "System" and branch_id == 1:
            raise ValidationError("No se puede eliminar sucursal System")

