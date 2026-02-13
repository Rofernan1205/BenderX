from sqlalchemy.orm import Session
from app.models.roles import Role

class RoleRepository:

    @staticmethod
    def get_role_by_name(db: Session, name: str):
        return db.query(Role).filter(Role.name == name).first()

    @staticmethod
    def get_all_roles(db: Session):
        return db.query(Role).all()

    @staticmethod
    def get_role_by_id(db: Session, id: int):
        return db.query(Role).filter(Role.id == id).first()

    @staticmethod
    def create_role(db: Session, **role_data):
        db_role = Role(**role_data)
        db.add(db_role)
        db.commit()
        db.refresh(db_role)
        return db_role

