import os
import sys
from alembic.config import Config
from alembic import command


def init_database():
    # 1. Ruta de la DB en AppData
    app_data = os.path.join(os.getenv('LOCALAPPDATA'), "BenderX")
    if not os.path.exists(app_data):
        os.makedirs(app_data)

    db_path = os.path.join(app_data, "benderx.db")
    db_url = f"sqlite:///{db_path}"

    # 2. Localizar alembic.ini (Subiendo un nivel si este archivo está en app/)
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        # Al estar en app/database_manager.py, subimos un nivel para llegar a la raíz
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    ini_path = os.path.join(base_path, "alembic.ini")

    cfg = Config(ini_path)
    cfg.set_main_option("sqlalchemy.url", db_url)
    cfg.set_main_option("script_location", os.path.join(base_path, "alembic"))

    try:
        command.upgrade(cfg, "head")
        return True, db_url
    except Exception as e:
        return False, str(e)