from sqlalchemy.orm import Session

from app.models import Role
from app.repositories.role_repository import RoleRepository
from app.models.roles import  Role

class RoleService:
    def __init__(self, db: Session):
        self._db = db
        self._role_rep = RoleRepository(db)

    def create_role(self, role_data: dict) -> Role | None:
        if self._role_rep.get_by_name(role_data['name']):
            raise ValueError(f"El rol ya existe {role_data['name']}")
        role = self._role_rep.create(role_data)
        return role

    def get_role(self, role_id: int) -> Role | None:
        role = self._role_rep.get_by_id(role_id)
        if not role:
            raise ValueError("Rol no existe")
        return role

    def get_roles(self) -> list[type[Role]]:
        roles = self._role_rep.get_all()
        return roles












        p
