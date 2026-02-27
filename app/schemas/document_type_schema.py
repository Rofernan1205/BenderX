from datetime import datetime
from typing import Optional
from pydantic import (BaseModel, Field
 , field_validator, ConfigDict)

class DocumentTypeBase(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=50)
    sequence_prefix: Optional[str] = Field(None, min_length=1, max_length=10)
    next_sequence: int = Field(default=1, ge=1) # ge numero >= 1
    requires_customer: bool = Field(default=False)
    is_credit_note: bool = Field(default=False)

    @field_validator('name', mode='before')
    @ classmethod
    def format_name(cls, v):
        if isinstance(v, str):
            return v.strip().title()
        return v

    @field_validator('sequence_prefix', mode='before')
    @ classmethod
    def format_sequence_prefix(cls, v):
        if isinstance(v, str):
            return v.strip().upper()
        return v

class DocumentTypeCreate(DocumentTypeBase):
    code: str = Field(..., min_length=2, max_length=20)
    name: str = Field(..., min_length=3, max_length=50)
    sequence_prefix: str = Field(..., min_length=1, max_length=10)

    @field_validator('code', mode='before')
    @ classmethod
    def format_code(cls, v):
        if isinstance(v, str):
            return v.strip()
        return v

    model_config = ConfigDict(
        str_strip_whitespace=True
    )


class DocumentTypeUpdate(DocumentTypeBase):
        is_active: Optional[bool] = None

        model_config = ConfigDict(
            str_strip_whitespace=True
        )

class DocumentTypeResponse(BaseModel):
        id: int
        code: str
        name: str
        sequence_prefix: str
        next_sequence: int
        requires_customer: bool
        is_credit_note: bool
        is_active: bool
        created_at: datetime
        updated_at: datetime

        model_config = ConfigDict(from_attributes=True)





