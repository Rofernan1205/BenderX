from sqlalchemy.orm import Session
from pydantic import ValidationError as PydanticError
from app.schemas.user_schema import UserCreate, UserUpdate, UserResponse
from app.models import User
from app.repositories.user_repository import UserRepository
from app.utils import security as Security
from app.core.exceptions import ValidationError, NotFoundError


class UserService:
    def __init__(self, db: Session):
        self._db = db
        self._repo = UserRepository(db)

    def create_user(self, user_data: dict) -> UserResponse:  # Retornamos el Schema de salida
        try:
            # 1. Validar datos con Pydantic
            validated_data = UserCreate(**user_data)

            # 2. Lógica de negocio (Verificar duplicados)
            if self._repo.get_by_username(validated_data.username):
                raise ValidationError(f"El usuario '{validated_data.username}' ya existe.")

            # 3. Preparar datos para la DB
            db_data = validated_data.model_dump()

            # 4. HASHEAR ANTES de enviar al repositorio
            if "password_hash" in db_data:
                db_data["password_hash"] = Security.hash_password(db_data["password_hash"])

            # 5. Persistencia
            new_user_obj = self._repo.create(db_data)

            return UserResponse.model_validate(new_user_obj)

        except PydanticError as e:
            raise ValidationError.from_pydantic(e)

    def update_user(self, user_id: int, user_data: dict) -> UserResponse:
        try:
            # 1. Validar entrada
            validated_data = UserUpdate(**user_data)

            # 2. Buscar si existe el usuario original
            user_obj = self._repo.get_by_id(user_id)
            if not user_obj:
                raise NotFoundError(f"El usuario con ID {user_id} no existe.")

            # 3. Detectar cambios reales (exclude_unset)
            clean_update_data = validated_data.model_dump(exclude_unset=True)

            if not clean_update_data:
                raise ValidationError("No se enviaron datos válidos para actualizar.")

            # 4. Si hay password nueva, se hashea
            if "password_hash" in clean_update_data:
                clean_update_data["password_hash"] = Security.hash_password(clean_update_data["password_hash"])

            # 5. Actualizar en el repositorio
            updated_user_obj = self._repo.update(user_obj, clean_update_data)


            return UserResponse.model_validate(updated_user_obj)

        except PydanticError as e:
            raise ValidationError.from_pydantic(e)























    # def __init__(self, db: Session):
    #     self._db = db
    #     self._repo = UserRepository(db)
    #
    # def create_user(self, user_data: dict) -> User :
    #     # 1. Validar usuario
    #     if self._repo.get_by_username(user_data.get("username")):
    #         raise ValidationError("Usuario ya existe")
    #     # Hashear la contraseña
    #     password = user_data.get("password")
    #     if password:
    #         user_data["password"] = Security.hash_password(password)
    #     user = self._repo.create(user_data)
    #     return user
    #
    #
    #
    # def update_user(self, user_id: int, update_data: dict) -> User :
    #
    #     user_obj = self._repo.get_by_id(user_id)
    #     if not user_obj:
    #         raise NotFoundError(f"Usuario con ID {user_id} no existe.")
    #
    #     if "password" in update_data and update_data["password"]:
    #         update_data["password"] = Security.hash_password(update_data["password"])
    #     elif "password" in update_data:
    #         del update_data["password"] # Elimina la clave del dict si viene vacio
    #
    #     # 3. Mapeo dinámico: Actualiza solo lo que viene en el dict
    #     for key, value in update_data.items():
    #         if hasattr(user_obj, key): # Sirve para no asignar  valores que no existan
    #             setattr(user_obj, key, value)
    #
    #     # 4. El repositorio sincroniza la Clase
    #     return self._repo.update(user_obj)
    #
    #
    # def delete_user(self, user_id: int):
    #
    #     user_obj = self._repo.get_by_id(user_id)
    #     if not user_obj:
    #         raise NotFoundError(f"Usuario con ID {user_id} no existe.")
    #
    #     if user_obj.role == "Admin" and user_id == 1:
    #         raise ValidationError("No se puede eliminar usuario Administrador")
    #
    #     return self._repo.delete(user_obj)
    #
    # def get_all_users(self, page: int = 1, limit: int = 20):
    #     return self._repo.get_all(page, limit)
    #
    # def get_user_by_id(self, user_id: int):
    #     return self._repo.get_by_id(user_id)
    #
    # def get_user_by_username(self, username: str):
    #     return self._repo.get_by_username(username)
