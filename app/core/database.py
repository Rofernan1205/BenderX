from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from app.core.config import settings

# Crear el Motor (Engine)
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {},
    echo=settings.DEBUG # Muestra el SQL en consola  solo en modo de desarrollo
)
# check_same_thread": False Deja  que cualquier hijo use el tunel

# Fábrica de Sesiones (SessionLocal)
session_factory= sessionmaker(
    autocommit=False, # NO guarda cambios automáticamente en la base de datos (session.commit())
    autoflush=False, # SQLAlchemy NO envía cambios automáticamente session.flush()
    bind=engine # Conexión a base de datos
)
# Esto garantiza que cada hilo (Thread) tenga su propia sesión independiente.
# Evita el error "Database is locked" cuando haces muchas operaciones.
SessionLocal = scoped_session(session_factory)

# Provee una sesión de base de datos de forma segura.
# Se asegura de cerrarla después de usarla para no consumir memoria.

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise "Error connecting to database"
    finally:
        db.close()