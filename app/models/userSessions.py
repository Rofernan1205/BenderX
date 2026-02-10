from datetime import datetime

from app.models import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import String, ForeignKey
from typing import  TYPE_CHECKING , Optional

if TYPE_CHECKING:
    from .users import  User
    from .branches import Branch
    from .cashSessions import CashSession
    # from .auditLog import AuditLog


class UserSession(Base):
    __tablename__ = "user_sessions"
    token:Mapped[str] = mapped_column(String(255), unique=True)
    ip_address:Mapped[Optional[str]] = mapped_column(String(45), nullable=True)
    computer_name : Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    exited_at: Mapped[Optional[datetime]] = mapped_column(nullable=True) # Fecha de salida

    user_id : Mapped[int] = mapped_column(ForeignKey('users.id'), ondelete='CASCADE')
    branch_id : Mapped[int] = mapped_column(ForeignKey('branches.id'), ondelete='RESTRICT')

    user:Mapped["User"] = relationship(back_populates="user_sessions")
    branch:Mapped["Branch"] = relationship(back_populates="user_sessions")

    cash_sessions: Mapped["CashSession"]= relationship("CashSession", back_populates="user_session")
    # logs : Mapped["AuditLog"] = relationship(back_populates="user_session")

    def __repr__(self):
        return f"<UserSession {self.computer_name}>"

