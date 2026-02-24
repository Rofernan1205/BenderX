from typing import Optional
from sqlalchemy.orm import Session
from app.models.roles import Role


class RoleRepository:

    def __init__(self, db: Session):
        self._db = db   #

    def get_all(self) -> list[type[Role]]:
        return self._db.query(Role).all()

    def get_by_id(self, role_id: int) -> Optional[Role]:
        return self._db.query(Role).filter(Role.id == role_id).first()

    def get_by_name(self, name: str) -> Optional[Role]:
        return self._db.query(Role).filter(Role.name == name).first()

    def create(self, role_data: dict) -> Role:
        role = Role(**role_data)
        self._db.add(role)
        self._db.flush()
        return role




