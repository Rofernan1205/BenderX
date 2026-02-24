from typing import Optional, List

from sqlalchemy.orm import Session
from pydantic import ValidationError as PydanticError

from app.models import User
from app.schemas.user_schema import UserCreate, UserUpdate, UserResponse
from app.repositories.user_repository import UserRepository
from app.utils import security
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
                db_data["password_hash"] = security.hash_password(db_data["password_hash"])

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
                clean_update_data["password_hash"] = security.hash_password(clean_update_data["password_hash"])

            # 5. Actualizar en el repositorio
            updated_user_obj = self._repo.update(user_obj, clean_update_data)


            return UserResponse.model_validate(updated_user_obj)

        except PydanticError as e:
            raise ValidationError.from_pydantic(e)

    def get_user(self, user_id: int) -> UserResponse:
        user_obj = self._repo.get_by_id(user_id)
        if not user_obj:
            raise NotFoundError(f"El usuario con ID {user_obj.id} no existe.")
        return UserResponse.model_validate(user_obj)

    def get_username(self, user_username: str) -> Optional[str]:
        user_obj = self._repo.get_by_username(user_username)
        if not user_obj:
            raise NotFoundError(f"El usuario  {user_username} no existe.")
        return user_obj.username

    def get_email(self, user_email: str) -> Optional[str]:
        user_obj = self._repo.get_by_email(user_email)
        if not user_obj:
            raise NotFoundError(f"El ucuario con email {user_email} no existe.")
        return user_obj.email

    def get_all_user(self, page: int = 1, limit: int = 20) -> List[UserResponse]:
        users = self._repo.get_all(page=page, limit=limit)
        return [UserResponse.model_validate(user) for user in users ]


    def delete_user(self, user_id: int) -> None:
        user_obj = self._repo.get_by_id(user_id)
        if not user_obj:
            raise NotFoundError(f"El usuario con id {user_obj.id} no existe.")
        if user_obj.role == "Admin" and user_id == 1:
            raise ValidationError("No se puede eliminar usuario Administrador")
        self._repo.delete(user_obj)

    def authenticate_user(self, username: str, password_plana: str) -> Optional[UserResponse]:
        user_obj = self._repo.get_by_username(username)
        if not user_obj:
            raise NotFoundError(f"El usuario {username} no existe.")
        if not security.verify_password(password_plana, user_obj.password_hash):
            raise ValidationError(f"La contraseña es incorrecta.")
        return UserResponse.model_validate(user_obj)



