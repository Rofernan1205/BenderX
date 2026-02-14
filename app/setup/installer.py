from app.core.database import SessionLocal
from app.models import Role
from app.services.role_service import RoleService



def install_system():

    with SessionLocal() as db:
        try:
            existing_role = db.query(Role).filter(Role.name == "Admin").first()
            if existing_role:
                print("Sistema ya instalado")
                return

            role_service = RoleService(db)

            role_service.create_role({"name": "Admin"})
            role_service.create_role({"name": "Dueño"})
            role_service.create_role({"name": "Supervisor"})
            role_service.create_role({"name": "Cajero"})

            db.commit()

            print("✅ Sistema instalado correctamente.")

        except Exception as e:
            db.rollback()
            raise ValueError(f"Error en carga de datos iniciales: {e}")
