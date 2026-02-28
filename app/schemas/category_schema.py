from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, field_validator, ConfigDict

class CategoryBase(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=50)
    description: Optional[str] = Field(None, max_length=500)
    is_active: bool = Field(default=True)

    @field_validator('name', mode='before')
    @classmethod
    def format_name(cls, v):
        if isinstance(v, str):
            return v.strip().upper()
        return v

class CategoryCreate(CategoryBase):
    name : str = Field(..., min_length=3, max_length=50)

    model_config = ConfigDict(
        str_strip_whitespace=True,
    )

class CategoryUpdate(CategoryBase):
    pass
    model_config = ConfigDict(
        str_strip_whitespace=True
    )
class CategoryResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
