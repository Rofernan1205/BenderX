from typing import NoReturn
from pydantic import ValidationError as PydanticError

class BenderXError(Exception):
    """
    CLASE BASE: Es la madre de todas las excepciones de BenderX.
    Se usa para capturar cualquier error propio del sistema de forma genérica.
    """
    def __init__(self, message="Ha ocurrido un error en el sistema"):
        self.message = message
        super().__init__(self.message)

class ValidationError(BenderXError):
    """
    ERRORES DE LÓGICA DE NEGOCIO O DATOS:
    Se usa cuando los datos enviados por el usuario no cumplen las reglas.
    Ejemplos:
    - Stock insuficiente para una venta.
    - Contraseña demasiado corta.
    - Fecha de compra es mayor a la fecha actual.
    - Campo obligatorio que viene vacío.
    """
    @staticmethod
    def from_pydantic(e: PydanticError) -> NoReturn:
        """
        Toma un PydanticError y lo lanza como una ValidationError de BenderX.
        """
        error_detail = e.errors()[0]
        # Extraemos el campo y el mensaje limpio
        campo = error_detail['loc'][0]
        mensaje = error_detail['msg'].replace("Value error, ", "")

        # Lanzamos la propia clase con el mensaje formateado
        raise ValidationError(f"Error en '{campo}': {mensaje}")

class NotFoundError(BenderXError):
    """
    RECURSO NO ENCONTRADO:
    Se usa cuando se busca un registro por ID o código y no existe.
    Ejemplos:
    - Buscar un producto por código de barras y que no esté en la DB.
    - Intentar editar un cliente que no existe.
    - Cargar una sucursal con un ID inválido.
    """
    pass

class DuplicateEntryError(BenderXError):
    """
    REGISTROS DUPLICADOS:
    Se usa cuando se intenta crear algo que ya existe y debe ser único.
    Ejemplos:
    - Registrar un usuario con un correo que ya está en uso.
    - Crear una sucursal con el mismo nombre que otra.
    - Ingresar un producto con un código SKU que ya existe.
    """
    pass

class DatabaseError(BenderXError):
    """
    ERRORES TÉCNICOS DE PERSISTENCIA:
    Se usa cuando el problema no es el dato, sino la infraestructura.
    Ejemplos:
    - El servidor de base de datos está apagado.
    - Error de conexión a la red.
    - El disco duro está lleno y no permite escribir más.
    """
    pass

class AuthenticationError(BenderXError):
    """
    ERRORES DE LOGIN:
    Se usa específicamente para el proceso de entrada al sistema.
    Ejemplos:
    - Usuario no existe al intentar loguearse.
    - La contraseña no coincide con el hash guardado.
    """
    pass

class AccessDeniedError(BenderXError):
    """
    ERRORES DE PERMISOS (AUTORIZACIÓN):
    Se usa cuando el usuario sí está logueado, pero no tiene nivel suficiente.
    Ejemplos:
    - Un cajero intenta abrir el módulo de "Configuración de Impuestos".
    - Un vendedor intenta eliminar una sucursal.
    """
    pass
