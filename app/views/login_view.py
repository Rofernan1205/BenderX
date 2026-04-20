from PySide6.QtWidgets import QMainWindow
from app.ui_py.login_ui import Ui_MainWindow # Importar al archivo login.py



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
        usuario = self.ui.lineEdit_username.text().strip()
        password = self.ui.lineEdit_password.text().strip()

        # 3. Verificación rápida por consola
        print(f"--- Datos capturados ---")
        print(f"Usuario: {usuario}")
        print(f"Password: {password}")

        # Ejemplo simple: si están vacíos, avisar en el label rojo
        if not usuario or not password:
            self.ui.labelError.setText("Debe completar todos los campos")
        else:
            self.ui.labelError.setText("")
            print("Datos listos para enviar al Service...")


