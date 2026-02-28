from decimal import Decimal
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict, field_validator


class PaymentMethodBase(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=50)
    fee_percentage: Decimal = Field(default=Decimal("0.00"), ge=0)
    fee_fixed: Decimal = Field(default=0.0, ge=0)
    requires_reference: bool = Field(default=False)
    allows_installments: bool = Field(default=False)
    max_installments: Optional[int] = Field(None, ge=1)
    is_active: bool = Field(default=True)

    @field_validator('name', mode='before')
    @classmethod
    def format_name(cls, v):
        if isinstance(v, str):
            return v.strip().upper()
        return v


class PaymentMethodCreate(PaymentMethodBase):
    # Campos obligatorios para insertar
    code: str = Field(..., min_length=1, max_length=20)
    name: str = Field(..., min_length=3, max_length=50)

    @field_validator('code')
    @classmethod
    def validate_code_numeric(cls, v: str):
        # En Perú muchos códigos SUNAT son numéricos (008, 005...)
        if not v.isdigit():
            raise ValueError("El código del método de pago debe contener solo números.")
        return v

    model_config = ConfigDict(
        str_strip_whitespace=True,
    )




class PaymentMethodUpdate(PaymentMethodBase):
    model_config = ConfigDict(
        str_strip_whitespace=True,
    )


class PaymentMethodResponse(BaseModel):
    id: int
    code: str
    name: str
    fee_percentage: Decimal
    fee_fixed: Decimal
    requires_reference: bool
    allows_installments: bool
    max_installments: Optional[int]
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )