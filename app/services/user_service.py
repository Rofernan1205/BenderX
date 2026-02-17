from sqlalchemy.orm import Session

from app.models import User
from app.repositories.user_repository import UserRepository
from app.utils import security as Security
from app.core.exceptions import ValidationError, NotFoundError, UserNotFoundException

class UserService:
    def __init__(self, db: Session):
        self._db = db
        self._repo = UserRepository(db)

    def create_user(self, user_data: dict) -> User | None:
        # 1. Validar usuario
        if self._repo.get_by_username(user_data.get("username")):
            raise ValidationError("Usuario ya existe")
        # Hashear la contraseña
        password = user_data.get("password")
        if password:
            user_data["password"] = Security.hash_password(password)
        user = self._repo.create(user_data)
        return user



    def update_user(self, user_id: int, update_data: dict):

        user_obj = self._repo.get_by_id(user_id)
        if not user_obj:
            raise UserNotFoundException(f"Usuario con ID {user_id} no existe.")

        if "password" in update_data and update_data["password"]:
            update_data["password"] = Security.hash_password(update_data["password"])
        elif "password" in update_data:
            del update_data["password"] # Elimina la clave del dict si viene vacio

        # 3. Mapeo dinámico: Actualiza solo lo que viene en el dict
        for key, value in update_data.items():
            if hasattr(user_obj, key): # Sirve para no asignar  valores que no existan
                setattr(user_obj, key, value)

        # 4. El repositorio sincroniza la Clase
        return self._repo.update(user_obj)


    def delete_user(self, user_id: int):

        user_obj = self._repo.get_by_id(user_id)
        if not user_obj:
            raise UserNotFoundException()

        if user_obj.role == "Admin" and user_id == 1:
            raise ValidationError("No se puede eliminar usuario Administrador")

        return self._repo.delete(user_obj)

    def get_all_users(self, page: int = 1, limit: int = 20):
        return self._repo.get_all(page, limit)

    def get_user_by_id(self, user_id: int):
        return self._repo.get_by_id(user_id)

    def get_user_by_username(self, username: str):
        return self._repo.get_by_username(username)
