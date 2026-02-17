from app.core.database import SessionLocal
from app.models import Role
from app.models import User
from app.services.role_service import RoleService
from app.services.user_service import UserService



roles = ["Administrador", "Dueño", "Supervisor", "Cajero"]

def install_system():

    with SessionLocal() as db:
        try:
            existing_role = db.query(Role).filter(Role.name == "Admin").first()
            if existing_role:
                print("Sistema ya instalado")
                return

            role_service = RoleService(db)
            user_service = UserService(db)

            for role in roles:
                role_service.create_role({"name": role})
            role_id = role_service.get_role(1)
            user_service.create_user({"username": "admin", "password": ""})




            db.commit()
            print("Datos iniciales OK ")

        except Exception as e:
            db.rollback()
            raise ValueError(f"Error en carga de datos iniciales: {e}")
