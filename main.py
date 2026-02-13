import sys
from app.database_manager import init_database

def main():

    print("Verificando base de datos...")
    exito, resultado = init_database()

    if not exito:
        print(f"ERROR CRÍTICO: No se pudo configurar la base de datos.\n{resultado}")
        # En una app de escritorio, aquí podrías usar un messagebox de Tkinter o PySide
        sys.exit(1)


    print(f"Conexión exitosa: {resultado}")

    # 3. Aquí lanzas tu aplicación principal
    print("Iniciando BenderX...")
    # Ejemplo:
    # app = MiAplicacionGUI()
    # app.run()

if __name__ == "__main__":
    main()




