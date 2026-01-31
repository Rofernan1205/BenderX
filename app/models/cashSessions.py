from datetime import datetime
from typing import List, Optional, TYPE_CHECKING
from sqlalchemy import String, ForeignKey, DateTime, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

if TYPE_CHECKING:
    from .branches import Branch
    from .users import  User
    from .cashRegisters import  CashRegister
    


class CashRegister(Base):
    __tablename__ = "cash_registers"




    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id", ondelete="CASCADE"))

    # 2. Con Sucursal (¿Desde dónde entró físicamente?)
    # ondelete="RESTRICT" porque no puedes borrar una sucursal con historial de acceso
    sucursal_id: Mapped[int] = mapped_column(ForeignKey("sucursales.id", ondelete="RESTRICT"))

    # --- CAMPOS DE AUDITORÍA ---
    fecha_ingreso: Mapped[datetime] = mapped_column(server_default=func.now())
    fecha_salida: Mapped[Optional[datetime]] = mapped_column(nullable=True)
    ip_cliente: Mapped[Optional[str]] = mapped_column(String(45))  # IP local o pública
    nombre_equipo: Mapped[Optional[str]] = mapped_column(String(100))  # Nombre PC (ej: CAJA-01)
    is_active: Mapped[bool] = mapped_column(default=True)

    # --- DEFINICIÓN DE RELACIONES (Relationship) ---
    usuario: Mapped["Usuario"] = relationship(back_populates="sesiones")
    sucursal: Mapped["Sucursal"] = relationship(back_populates="sesiones")

    # Relación con Logs: Para saber qué se hizo DURANTE esta sesión
    logs: Mapped[List["LogActividad"]] = relationship(back_populates="sesion", cascade="all, delete-orphan")