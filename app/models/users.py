from app.models import Base
from typing import List, TYPE_CHECKING, Optional
from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column


class User(Base):
    __tablename__ = "users"
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    last_name: Mapped[str] = mapped_column(String(80), nullable=False)
    username: Mapped[str] = mapped_column(String(15), nullable=False, unique=True, index=True)
    password: Mapped[str] = mapped_column(String(25), nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(15),nullable=False)
    address: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    branch_id :Mapped[int] = mapped_column(ForeignKey('branches.id'), nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey('roles.id'), nullable=False)



    def __repr__(self) -> str:
        return f"<Users {self.name}, {self.last_name}, {self.username}> >"

