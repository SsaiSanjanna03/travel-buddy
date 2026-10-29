from math import asin, cos, radians, sin, sqrt
from typing import Optional

from app.models import Place


# Fictional sample records for development only.
# Replace them with verified, permitted data before production use.
SAMPLE_PLACES = [
    Place(
        id=1,
        name="Sample Coffee Shop",
        city="Ames",
        category="coffee",
        latitude=42.03,
        longitude=-93.62,
        description="Fictional sample coffee listing.",
        source="sample",
    ),
    Place(
        id=2,
        name="Sample Local Restaurant",
        city="Ames",
        category="food",
        latitude=42.02,
        longitude=-93.64,
        description="Fictional sample restaurant listing.",
        source="sample",
    ),
    Place(
        id=3,
        name="Sample Juice Bar",
        city="Des Moines",
        category="drinks",
        latitude=41.59,
        longitude=-93.62,
        description="Fictional sample drinks listing.",
        source="sample",
    ),
]


def distance_km(
    lat1: float,
    lon1: float,
    lat2: float,
    lon2: float,
) -> float:
    """Calculate approximate great-circle distance using the Haversine formula."""
    earth_radius_km = 6371.0

    lat1_rad = radians(lat1)
    lat2_rad = radians(lat2)
    delta_lat = radians(lat2 - lat1)
    delta_lon = radians(lon2 - lon1)

    haversine = (
        sin(delta_lat / 2) ** 2
        + cos(lat1_rad) * cos(lat2_rad) * sin(delta_lon / 2) ** 2
    )
    haversine = min(1.0, max(0.0, haversine))

    return 2 * earth_radius_km * asin(sqrt(haversine))


def search_places(
    city: Optional[str] = None,
    category: Optional[str] = None,
    lat: Optional[float] = None,
    lon: Optional[float] = None,
    radius_km: Optional[float] = None,
) -> list[Place]:
    """Filter sample places by city, category, and optional geographic radius."""
    results = SAMPLE_PLACES.copy()

    if city:
        city_query = city.strip().casefold()
        results = [
            place for place in results
            if place.city.casefold() == city_query
        ]

    if category:
        category_query = category.strip().casefold()
        results = [
            place for place in results
            if place.category == category_query
        ]

    if lat is not None and lon is not None and radius_km is not None:
        results = [
            place for place in results
            if distance_km(
                lat,
                lon,
                place.latitude,
                place.longitude,
            ) <= radius_km
        ]

    return results
