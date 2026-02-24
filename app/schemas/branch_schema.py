from typing import Optional
from pydantic import BaseModel, Field, EmailStr, field_validator, ConfigDict


# --- ESQUEMA BASE ---
class BranchBase(BaseModel):
    # Usamos Optional y None para que el Update no obligue a enviarlos
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    phone: Optional[str] = Field(None, pattern=r'^\d{7,15}$')
    email: Optional[EmailStr] = None
    address: Optional[str] = Field(None, max_length=255)

    # Normalización

    @field_validator('name')
    @classmethod
    def format_name(cls, v: Optional[str]):
        if v:
            return v.strip().title()
        return v

    @field_validator('email')
    @classmethod
    def format_email(cls, v: Optional[str]):
        if v:
            return v.strip().lower()
        return v

    @field_validator('phone')
    @classmethod
    def format_phone(cls, v: Optional[str]):
        if v:
            return v.strip().replace(' ', '')
        return v


# --Create datos  obligatorios
# --Sobreescribimos para quitar el Optional y el None
class BranchCreate(BranchBase):
    name: str = Field(..., min_length=3, max_length=100)
    phone: str = Field(..., pattern=r'^\d{7,15}$')
    email: EmailStr # Requerido por defecto al no tener default
    model_config = ConfigDict(
        populate_by_name=True, # Habilita la flexibilidad de nombres
        str_strip_whitespace=True
    )

# Dejamos sin datos por que hereda de la clase padre
class BranchUpdate(BranchBase):
    model_config = ConfigDict(
        populate_by_name=True, # Habilita la flexibilidad de nombres
        str_strip_whitespace=True
    )


class BranchResponse(BranchBase):
    id: int
    model_config = ConfigDict(from_attributes=True)  # Crucial para leer de SQLAlchemy