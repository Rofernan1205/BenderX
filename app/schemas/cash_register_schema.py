from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, field_validator, ConfigDict

class CashRegisterBase(BaseModel):
    name: Optional[str] = Field(None, min_length=3 ,max_length=50)
    device_code: Optional[str] = Field(None, min_length=3 ,max_length=50)

    # --- Normalizaciones ---
    @field_validator('name', mode='before')
    @classmethod
    def format_name(cls, v):
        return v.title().strip() if isinstance(v, str) else v

    # --- Normalizaciones ---
    @field_validator('device_code', mode='before')
    @classmethod
    def format_device_code(cls, v):
        return v.upper().strip() if isinstance(v, str) else v


class CashRegisterCreate(CashRegisterBase):
    name: str = Field(..., min_length=3, max_length=50)
    device_code: str = Field(..., min_length=3, max_length=50)
    user_id: int = Field(..., gt=0)
    branch_id: int = Field(..., gt=0)

    model_config = ConfigDict(
        str_strip_whitespace=True
    )

class CashRegisterUpdate(CashRegisterBase):
    user_id: Optional[int] = Field(None, gt=0)
    branch_id: Optional[int] = Field(None, gt=0)

    model_config = ConfigDict(
        str_strip_whitespace=True
    )

class CashRegisterResponse(BaseModel):
    id : int
    name: str
    device_code: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
    user_id: int
    branch_id: int
    model_config = ConfigDict(from_attributes=True)
