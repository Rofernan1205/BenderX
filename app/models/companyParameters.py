from app.models import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String,Text
from typing import Optional

class CompanyParameter(Base):
    __tablename__ = "company_parameters"
    name : Mapped[str] = mapped_column(String(200), nullable=False)
    ruc: Mapped[str] = mapped_column(String(20),nullable=False)
    config_json: Mapped[Optional[str]] = mapped_column(Text)

    def __repr__(self) -> str:
        return f"CompanyParameter('{self.name}', {self.ruc})"


