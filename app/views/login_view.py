from PySide6.QtWidgets import QMainWindow
from app.ui_py.login_ui import Ui_MainWindow # Importar al archivo login.py

from app.core.database import SessionLocal
from app.services.user_service import UserService
from pydantic import ValidationError as PydanticError
from app.core.exceptions import ValidationError, NotFoundError



class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Usamos la clase generada por Qt Designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 1. Conectamos el botón con la función de lectura
        self.ui.buttonSession.clicked.connect(self.leer_formulario)

        # Limpiamos el label de error por si tiene texto de prueba
        self.ui.labelError.setText("")

    def leer_formulario(self):
        # 2. Obtenemos el texto de los QLineEdit
        username = self.ui.lineEdit_username.text().strip()
        password = self.ui.lineEdit_password.text().strip()

        if not username or not password:
            self.ui.labelError.setText("Complete todos los campos")
            return

        with SessionLocal() as db:
            try:
                users_service = UserService(db)
                validated_user = users_service.authenticate_user(username, password)
                print(validated_user)
            except (NotFoundError, ValidationError) as err:
                self.ui.labelError.setText(str(err))






