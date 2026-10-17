from fastapi import FastAPI, HTTPException
from app.models import LocationQuery, VenueResponse
from app.services import RecommendationService
from typing import List

app = FastAPI(
    title="Vyoma LLC — Spatial Recommendation API",
    description="Location-based social trend aggregation platform for must-try food and beverage experiences.",
    version="0.1.0"
)


@app.get("/", tags=["Health Check"])
def root():
    return {
        "status": "online",
        "service": "Vyoma API",
        "version": "0.1.0",
        "message": "Spatial Recommendation Engine is operational."
    }


@app.post("/api/v1/recommendations/nearby", response_model=List[VenueResponse], tags=["Recommendations"])
def get_nearby_recommendations(query: LocationQuery):
    """
    Accepts latitude and longitude coordinates and returns trending local food and drink recommendations.
    """
    try:
        recommendations = RecommendationService.get_nearby_must_tries(query)
        return recommendations
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error processing spatial query: {str(e)}")
