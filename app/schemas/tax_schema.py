from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field, field_validator, ConfigDict


class TaxBase(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=50)
    rate: Optional[Decimal] = Field(None, ge=0)
    is_percentage: Optional[bool] = Field(default=True)

    @field_validator('name', mode='before')
    @classmethod
    def format_name(cls, v):
        if isinstance(v, str):
            return v.strip().upper()
        return v


class TaxCreate(TaxBase):
    # Obligatorios para creación
    code: str = Field(..., min_length=1, max_length=20)
    name: str = Field(..., min_length=3, max_length=50)
    rate: Decimal = Field(..., ge=0)

    @field_validator('code')
    @classmethod
    def validate_code_numeric(cls, v: str):
        if not v.isdigit():
            raise ValueError("El código SUNAT debe contener solo números")
        return v

    model_config = ConfigDict(
        str_strip_whitespace=True,
    )


class TaxUpdate(TaxBase):
    # El código NO debe estar aquí para evitar que el usuario lo cambie
    model_config = ConfigDict(
        str_strip_whitespace=True,
    )

class TaxResponse(BaseModel):
    id: int
    code: str
    name: str
    rate: Decimal
    is_percentage: bool
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )









