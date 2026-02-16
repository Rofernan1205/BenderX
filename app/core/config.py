import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME: str = "BenderX"
    PROJECT_VERSION: str = "1.0.0"

    def __init__(self):
        self.BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
        self.LOG_DIR: Path = self.BASE_DIR / "logs"

        # 📌 Ruta dinámica en AppData (Windows)
        local_appdata = Path(os.getenv("LOCALAPPDATA"))
        self.APP_DIR = local_appdata / "BenderX"
        self.APP_DIR.mkdir(parents=True, exist_ok=True)

        self.DATABASE_PATH = self.APP_DIR / "benderx.db"
        self.DATABASE_URL = f"sqlite:///{self.DATABASE_PATH}"

        self._create_directories()

        self.SECRET_KEY: str = os.getenv(
            "SECRET_KEY",
            "dev_secret_key_change_me_in_production"
        )

        self.DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    def _create_directories(self):
        self.LOG_DIR.mkdir(exist_ok=True, parents=True)


settings = Settings()
