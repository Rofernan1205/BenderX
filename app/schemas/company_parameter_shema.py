import json
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict, field_validator


class CompanyConfig(BaseModel):
    """Estructura interna detallada para el campo config_json"""
    currency_symbol: str = Field(default="S/", min_length=1, max_length=5)
    currency_iso: str = Field(default="PEN", pattern=r"^[A-Z]{3}$")
    decimal_places: int = Field(default=2, ge=0, le=4)
    igv_percent: float = Field(default=18.0, ge=0)

    # Datos de contacto para comprobantes
    address: str = Field(default="DIRECCIÓN NO DEFINIDA", max_length=255)
    phone: Optional[str] = Field(default=None, max_length=20)
    email: Optional[str] = Field(default=None, max_length=100)

    # Ajustes del sistema (POS)
    low_stock_threshold: int = Field(default=5, ge=0)
    allow_negative_stock: bool = False

    model_config = ConfigDict(str_strip_whitespace=True)

class CompanyParameterBase(BaseModel):
    name: Optional[str] = Field(None, min_length=3 ,max_length=200)
    ruc : Optional[str] = Field(None, pattern=r"^\d{11}$")

    @field_validator('name', mode='before')
    @classmethod
    def format_name(cls, v):
        if isinstance(v, str):
            return v.title().strip()
        return v

    @field_validator('ruc', mode='before')
    @classmethod
    def format_ruc(cls, v):
        if isinstance(v, str):
            return v.strip()
        return v

class CompanyParameterCreate(CompanyParameterBase):
    name: str = Field(..., min_length=3, max_length=200)
    ruc: str = Field(..., pattern=r"^\d{11}$")
    model_config = ConfigDict(str_strip_whitespace=True)

class CompanyParameterUpdate(CompanyParameterBase):
    config_json: CompanyConfig
    model_config = ConfigDict(str_strip_whitespace=True)

class CompanyParameterResponse(BaseModel):
    id: int
    name: str
    ruc: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
    config_json: CompanyConfig

    @field_validator("config_json", mode="before")
    @classmethod
    def transform_string_to_json(cls, v):
        """
        Lógica Pro: Si SQLAlchemy devuelve un string (Text),
        lo convertimos a dict para que Pydantic lo valide.
        """
        if isinstance(v, str):
            try:
                return json.loads(v)
            except json.JSONDecodeError:
                # Si el JSON está corrupto o vacío, devolvemos valores por defecto
                return CompanyConfig().model_dump()
        return v

    model_config = ConfigDict(from_attributes=True)



