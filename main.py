import sys
from app.database_manager import init_database
from app.setup.installer import install_system


def main():

    print("Verificando base de datos...")
    success, result = init_database()

    if not success:
        print(f"ERROR CRÍTICO: No se pudo configurar la base de datos.\n{result}")
        # En una app de escritorio, aquí podrías usar un messagebox de Tkinter o PySide
        sys.exit(1)
    print(f"Conexión exitosa: {result}")
    install_system()

    # 3. Aquí lanzas tu aplicación principal
    print("Iniciando BenderX...")
    # Ejemplo:
    # app = MiAplicacionGUI()
    # app.run()

if __name__ == "__main__":
    main()




