from sqlalchemy.exc import IntegrityError
from app.core.database import SessionLocal
from app.models import Role, User
from app.services.role_service import RoleService
from app.services.user_service import UserService
from app.services.branch_service import BranchService
from app.setup.seed_data import  INITIAL_ROLES, INITIAL_BRANCH, SUPER_USER


def install_system():
    with SessionLocal() as db:
        try:
            # verificar usuario administrador existe
            user_exists = db.query(User).first()
            if user_exists:
                print("Sistema ya instalado.")
                return

            role_service = RoleService(db)
            branch_service = BranchService(db)
            user_service = UserService(db)

            print("Instalando sistema...")

            # 🔹 2. Crear roles si no existen
            for role_name in INITIAL_ROLES:
                existing = db.query(Role).filter(Role.name == role_name).first()
                if not existing:
                    role_service.create_role({"name": role_name})

            db.flush()

            # 3. Crear sucursal principal
            branch = branch_service.create_branch(INITIAL_BRANCH)

            db.flush()

            # 4. Obtener rol administrador por nombre
            admin_role = db.query(Role).filter(
                Role.name == "Administrador"
            ).first()

            user_data = SUPER_USER.copy()
            user_data["role_id"] = admin_role.id
            user_data["branch_id"] = branch.id

            #  5. Crear usuario administrador
            user_service.create_user(user_data)

            db.commit()
            print("Sistema instalado correctamente.")

        except IntegrityError:
            db.rollback()
            print("Datos ya existentes.")
        except Exception as e:
            db.rollback()
            raise RuntimeError(f"Error en instalación: {e}")
