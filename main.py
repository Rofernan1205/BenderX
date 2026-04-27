import sys
import os
from app.database_manager import init_database
from app.setup.installer import install_system


# Esto asegura que Python encuentre la carpeta 'app'
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from PySide6.QtWidgets import QApplication
from app.views.login_view import LoginWindow # importar login.ui


def main():

    print("Verificando base de datos...")
    success, result = init_database()

    if not success:
        print(f"ERROR CRÍTICO: No se pudo configurar la base de datos.\n{result}")
        # En una app de escritorio, aquí podrías usar un messagebox de Tkinter o PySide
        sys.exit(1)
    print(f"Conexión exitosa: {result}")
    install_system()


    #Crear la instancia de la aplicación
    app = QApplication(sys.argv)

    # Hoja de estilo
    load_stylesheet(app)

    # Instance nuestra clase de Login
    login = LoginWindow()

    # 3. Mostrar la ventana
    login.show()

    # 4. Iniciar el bucle de eventos
    sys.exit(app.exec())

# Conexión a hoja de estilos general
def load_stylesheet(app):
    path_styles = os.path.join("app", "styles", "styles.qss")
    if os.path.exists(path_styles):
        with open(path_styles, "r") as f:
            app.setStyleSheet(f.read())
    else:
        print("No se encuentra hoja de estilos")




if __name__ == "__main__":
    main()





