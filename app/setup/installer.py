from app.core.database import SessionLocal
from app.models import Role
from app.models import User
from app.models import Branch
from app.services.role_service import RoleService
from app.services.user_service import UserService
from app.services.branch_service import BranchService



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
            branch_service = BranchService(db)

            for role in roles:
                role_service.create_role({"name": role})
            role_id = role_service.get_role(1)
            branch_service.create_branch({"name" : "  Sistema", "phone": " 94656643834", "email": "example@hotmail.com"})
            #/ user_service.create_user({"username": "admin", "password": ""})




            db.commit()
            print("Datos iniciales OK ")

        except Exception as e:
            db.rollback()
            raise ValueError(f"Error en carga de datos iniciales: {e}")
