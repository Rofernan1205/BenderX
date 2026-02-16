from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.utils.security import hash_password, verify_password
from app.core.exceptions import UserNotFoundException, ValidationError

class UserService:
    def __init__(self, db: Session):
        self._db = db
        self._repo = UserRepository(db)

    def create_user(self, user_data: dict):
        """
        PROCESO: Recibe Dict -> Valida -> Hashea -> Repo.create(Dict)
        """
        # 1. Validar si el correo ya existe
        if self._repo.get_by_email(user_data.get("email")):
            raise ValidationError("Este correo electrónico ya está en uso.")

        # 2. Hashear la contraseña (Seguridad)
        if "password" in user_data:
            user_data["password"] = Security.hash_password(user_data.pop("password"))

        # 3. El repositorio crea el objeto a partir del Diccionario
        return self._repo.create(user_data)

    def update_user(self, user_id: int, update_data: dict):
        """
        PROCESO: Busca Clase -> Modifica Atributos -> Repo.update(Clase)
        """
        # 1. Obtener la clase (instancia activa de SQLAlchemy)
        user_obj = self._repo.get_by_id(user_id)
        if not user_obj:
            raise UserNotFoundException(f"Usuario con ID {user_id} no existe.")

        # 2. Si se intenta cambiar el password, hashearlo
        if "password" in update_data and update_data["password"]:
            update_data["password"] = Security.hash_password(update_data["password"])
        elif "password" in update_data:
            del update_data["password"] # Evita pisar con un valor vacío

        # 3. Mapeo dinámico: Actualiza solo lo que viene en el dict
        for key, value in update_data.items():
            if hasattr(user_obj, key):
                setattr(user_obj, key, value)

        # 4. El repositorio sincroniza la Clase
        return self._repo.update(user_obj)

    def delete_user(self, user_id: int):
        """
        PROCESO: Busca Clase -> Valida Reglas -> Repo.delete(Clase)
        """
        user_obj = self._repo.get_by_id(user_id)
        if not user_obj:
            raise UserNotFoundException()

        # Regla de Oro: No borrar al sistema o admins críticos
        if user_obj.role == "Admin" and user_id == 1:
            raise ValidationError("No se puede eliminar al administrador raíz.")

        return self._repo.delete(user_obj)

    def get_all_users(self, page: int = 1, limit: int = 20):
        skip = (page - 1) * limit
        return self._repo.get_all(skip=skip, limit=limit)