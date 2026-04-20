from PySide6.QtWidgets import QMainWindow
from app.ui_py.login_ui import Ui_MainWindow


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Usamos la clase generada por Qt Designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Opcional: Quitar bordes de ventana si hiciste un diseño personalizado
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)

        print("Login cargado correctamente")