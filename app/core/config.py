import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME: str = "BenderX"
    PROJECT_VERSION: str = "1.0.0"

    # 1. Rutas con validación
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
    DATA_DIR: Path = BASE_DIR / "data"
    LOG_DIR: Path = BASE_DIR / "logs"

    def __init__(self):
        # Creamos las carpetas al instanciar, no al definir
        self._create_directories()

    def _create_directories(self):
        """Crea las carpetas necesarias para la persistencia y auditoría."""
        for directory in [self.DATA_DIR, self.LOG_DIR]:
            directory.mkdir(exist_ok=True, parents=True)

    # 2. Conexión a la base de datos con Fallback seguro
    DATABASE_URL: str = os.getenv("DATABASE_URL", f"sqlite:///{DATA_DIR}/benderx.db")

    # 3. Seguridad obligatoria para cobros e internet
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev_secret_key_change_me_in_production")

    # 4. Flags de estado
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"


# INSTANCIA GLOBAL
settings = Settings()