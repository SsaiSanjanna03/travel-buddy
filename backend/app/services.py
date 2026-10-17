import math
from typing import List
from app.models import LocationQuery, VenueResponse, RecommendedItem


def calculate_haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the great-circle distance between two points on the Earth in meters.
    """
    R = 6371000.0  # Earth radius in meters
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * \
        math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


class RecommendationService:
    @staticmethod
    def get_nearby_must_tries(query: LocationQuery) -> List[VenueResponse]:
        # Mock dataset representing aggregated social media venue trends
        mock_venues = [
            {
                "venue_id": "v101",
                "name": "Piazza Espresso Bar",
                "address": "Via Roma 12, Milan, Italy",
                "latitude": query.latitude + 0.001,
                "longitude": query.longitude + 0.001,
                "items": [
                    RecommendedItem(
                        item_name="Pistachio Cornetto",
                        category="Pastry",
                        social_score=9.8,
                        trending_reason="Viral on Instagram Reels with 50K+ saves this month"
                    ),
                    RecommendedItem(
                        item_name="Shakerato Espresso",
                        category="Coffee",
                        social_score=9.2,
                        trending_reason="Top recommended local summer coffee drink"
                    )
                ]
            },
            {
                "venue_id": "v102",
                "name": "Trattoria del Centro",
                "address": "Piazza Duomo 5, Milan, Italy",
                "latitude": query.latitude - 0.002,
                "longitude": query.longitude + 0.0015,
                "items": [
                    RecommendedItem(
                        item_name="Risotto alla Milanese",
                        category="Main Course",
                        social_score=9.6,
                        trending_reason="Consistently tagged as the best saffron risotto in town"
                    )
                ]
            }
        ]

        results = []
        for venue in mock_venues:
            dist = calculate_haversine_distance(
                query.latitude, query.longitude, venue["latitude"], venue["longitude"]
            )
            if dist <= query.radius_meters:
                results.append(
                    VenueResponse(
                        venue_id=venue["venue_id"],
                        name=venue["name"],
                        address=venue["address"],
                        latitude=venue["latitude"],
                        longitude=venue["longitude"],
                        distance_meters=round(dist, 1),
                        must_try_items=venue["items"]
                    )
                )

        return results
