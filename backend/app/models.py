from typing import List, Optional
from pydantic import BaseModel, Field


class LocationQuery(BaseModel):
    latitude: float = Field(..., ge=-90.0, le=90.0,
                            description="Latitude coordinate")
    longitude: float = Field(..., ge=-180.0, le=180.0,
                             description="Longitude coordinate")
    radius_meters: Optional[int] = Field(
        default=1000, ge=100, le=10000, description="Search radius in meters")


class RecommendedItem(BaseModel):
    item_name: str = Field(..., description="Name of the food or drink")
    category: str = Field(...,
                          description="Category e.g., Coffee, Pasta, Gelato, Cocktail")
    social_score: float = Field(
        ..., description="Aggregated recommendation score from social signals")
    trending_reason: str = Field(...,
                                 description="Summary of why it is viral on social media")


class VenueResponse(BaseModel):
    venue_id: str
    name: str
    address: str
    latitude: float
    longitude: float
    distance_meters: float
    must_try_items: List[RecommendedItem]
