from alembic.config import Config
from alembic import command
from app.core.config import settings
import os
import sys


def init_database():

    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    ini_path = os.path.join(base_path, "alembic.ini")

    cfg = Config(ini_path)
    cfg.set_main_option("sqlalchemy.url", settings.DATABASE_URL)
    cfg.set_main_option("script_location", os.path.join(base_path, "alembic"))

    try:
        command.upgrade(cfg, "head")
        return True, settings.DATABASE_URL
    except Exception as e:
        return False, str(e)
