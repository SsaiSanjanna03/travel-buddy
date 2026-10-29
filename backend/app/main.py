from typing import Optional

from fastapi import FastAPI, HTTPException, Query

from app.models import Place
from app.services import search_places


app = FastAPI(
    title="Travel Discovery API",
    description="Initial API prototype for discovering local food and drinks.",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    """Return a basic application health status."""
    return {"status": "ok"}


@app.get("/places", response_model=list[Place])
def get_places(
    city: Optional[str] = Query(default=None, min_length=1, max_length=100),
    category: Optional[str] = Query(default=None),
    lat: Optional[float] = Query(default=None, ge=-90, le=90),
    lon: Optional[float] = Query(default=None, ge=-180, le=180),
    radius_km: Optional[float] = Query(default=None, gt=0, le=20000),
) -> list[Place]:
    """Return places matching the provided optional filters."""
    if category is not None:
        category = category.strip().casefold()
        if category not in {"food", "coffee", "drinks"}:
            raise HTTPException(
                status_code=422,
                detail="category must be food, coffee, or drinks",
            )

    if (lat is None) != (lon is None):
        raise HTTPException(
            status_code=422,
            detail="lat and lon must be provided together",
        )

    if radius_km is not None and lat is None:
        raise HTTPException(
            status_code=422,
            detail="radius_km requires both lat and lon",
        )

    return search_places(
        city=city,
        category=category,
        lat=lat,
        lon=lon,
        radius_km=radius_km,
    )
