from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, EmailStr, field_validator, ConfigDict


class UserBase(BaseModel):
    # En la Base, password_hash NO debe estar por seguridad
    name: Optional[str] = Field(None, min_length=3, max_length=80)
    last_name: Optional[str] = Field(None, min_length=3, max_length=80)
    email: Optional[EmailStr] = None
    dni: Optional[str] = Field(None, pattern=r'^\d{8}$', description='DNI 8 digitos')
    username: Optional[str] = Field(None, min_length=4, max_length=25)
    phone: Optional[str] = Field(None, pattern=r'^\d{7,15}$')
    address: Optional[str] = Field(None, max_length=255)

    # --- Normalizaciones ---
    @field_validator('name', 'last_name', mode='before')
    @classmethod
    def format_name(cls, v):
        return v.title().strip() if isinstance(v, str) else v

    @field_validator('email', 'username', 'dni', mode='before')
    @classmethod
    def format_to_lower(cls, v):
        return v.strip().lower() if isinstance(v, str) else v

    @field_validator('phone', mode='before')
    @classmethod
    def format_phone(cls, v):
        return v.strip().replace(' ', '') if isinstance(v, str) else v


class UserCreate(UserBase):
    # 1. Hacemos obligatorios los campos para la creación
    name: str = Field(..., min_length=3, max_length=80)
    last_name: str = Field(..., min_length=3, max_length=80)
    email: EmailStr
    dni: str = Field(..., pattern=r'^\d{8}$')
    username: str = Field(..., min_length=4, max_length=25)
    phone: str = Field(..., pattern=r'^\d{7,15}$')
    role_id: int = Field(..., gt=0)
    branch_id: int = Field(..., gt=0)

    # 3. El password solo vive en Create y Update (con alias para el frontend)
    password_hash: str = Field(..., min_length=8, max_length=255, alias="password")

    model_config = ConfigDict(
        populate_by_name=True, # Habilita la flexibilidad de nombres
        str_strip_whitespace=True
    )


class UserUpdate(UserBase):
    # En Update todo es opcional
    password_hash: Optional[str] = Field(None, min_length=8, max_length=255, alias="password")
    role_id: Optional[int] = Field(None, gt=0)
    branch_id: Optional[int] = Field(None, gt=0)

    model_config = ConfigDict(populate_by_name=True, str_strip_whitespace=True)


class UserResponse(BaseModel):
    # 4. Lo que el API devuelve al mundo (Incluye IDs y fechas generadas)
    id: int
    name: str
    last_name: str
    username: str
    password_hash: str
    email: str
    phone: str
    dni : int
    address: Optional[str] = None
    last_login: Optional[datetime] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime
    role_id: int
    branch_id: int

    model_config = ConfigDict(from_attributes=True)  # Crucial para leer de SQLAlchemy











