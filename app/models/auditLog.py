from app.models.base import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import String, ForeignKey
from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from .users import  User
    from .userSessions import UserSession
    from .cashSessions import CashSession
    from .branches import Branch



class AuditLog(Base):
    __tablename__ = "audit_logs"
    action : Mapped[str] = mapped_column(String(40), nullable=False, index=True) # CREATE, UPDATE, DELETE , LOGIN
    entity : Mapped[str] = mapped_column(String(50), nullable=False) # Tabla afectada
    description : Mapped[Optional[str]] = mapped_column(String(100), nullable=True) # Descripción
    ip_address : Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    source : Mapped[Optional[str]] = mapped_column(String(50), nullable=True) # POS, ADMIN_PANEL, SYSTEM

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    user_session_id : Mapped[int] = mapped_column(ForeignKey("user_sessions.id"), nullable=True)
    cash_session_id : Mapped[int] = mapped_column(ForeignKey("cash_sessions.id"), nullable=True)
    branch_id : Mapped[int] = mapped_column(ForeignKey("branches.id"), nullable=True)

    user: Mapped["User"] = relationship()
    user_session: Mapped["UserSession"] = relationship()
    cash_register: Mapped["CashSession"] = relationship()
    branch : Mapped["Branch"] = relationship()


    def __repr__(self) -> str:
        return  f"< Audilog {self.action} , {self.entity} >"


