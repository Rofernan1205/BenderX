from sqlalchemy.exc import IntegrityError
from app.core.database import SessionLocal
from app.models import Role, User, DocumentType, Tax
from app.services.role_service import RoleService
from app.services.user_service import UserService
from app.services.branch_service import BranchService
from app.services.document_type_service import DocumentTypeService
from app.services.tax_service import TaxService
from app.setup.seed_data import  (
    INITIAL_ROLES,
    INITIAL_BRANCH,
    SUPER_USER,
    DOCUMENT_TYPES,
    INITIAL_TAXES)


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
            doct_type_service = DocumentTypeService(db)
            tax_service = TaxService(db)

            print("Iniciando instalación...")

            # Crear roles si no existen
            for role_name in INITIAL_ROLES:
                existing = db.query(Role).filter(Role.name == role_name).first()
                if not existing:
                    role_service.create_role({"name": role_name})
            db.flush()


            # Crear tipo de documento
            for doct_type in DOCUMENT_TYPES:
                existing = db.query(DocumentType).filter(DocumentType.name == doct_type["name"]).first()
                if not existing:
                        doct_type_service.create_doct_type(doct_type)
            db.flush()

            # crear impuestos
            for tax in INITIAL_TAXES:
                existing = db.query(Tax).filter(Tax.code == tax["code"]).first()
                if not existing:
                    tax_service.create_tax(tax)
            db.flush()

            # Crear sucursal principal
            branch = branch_service.create_branch(INITIAL_BRANCH)
            db.flush()

            # Obtener rol administrador por nombre
            admin_role = db.query(Role).filter(
                Role.name == "Administrador"
            ).first()

            user_data = SUPER_USER.copy()
            user_data["role_id"] = admin_role.id
            user_data["branch_id"] = branch.id

            # Crear usuario administrador
            user_service.create_user(user_data)

            db.commit()
            print("Sistema instalado correctamente.")

        except IntegrityError:
            db.rollback()
            print("Datos ya existentes.")
        except Exception as e:
            db.rollback()
            raise RuntimeError(f"Error en instalación: {e}")
