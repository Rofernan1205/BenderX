
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import List, TYPE_CHECKING

from app.models import Base
if TYPE_CHECKING:
    from .users import User



class Rol(Base):
    __tablename__ = 'roles'
    name : Mapped[str] = mapped_column(String(60), nullable=False, index=True, unique=True)
    # Relationship
    users: Mapped[List["User"]] = relationship(back_populates="rol")

    def __repr__(self) -> str:
        return f"<Role {self.name}>"

