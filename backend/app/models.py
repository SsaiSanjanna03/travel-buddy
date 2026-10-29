from typing import Literal

from pydantic import BaseModel, Field, field_validator


PlaceCategory = Literal["food", "coffee", "drinks"]


class Place(BaseModel):
    id: int
    name: str = Field(min_length=1, max_length=150)
    city: str = Field(min_length=1, max_length=100)
    category: PlaceCategory
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    description: str = Field(default="", max_length=1000)
    source: str = Field(default="sample", min_length=1, max_length=100)

    @field_validator("name", "city", "source")
    @classmethod
    def strip_required_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Value cannot be blank")
        return value
