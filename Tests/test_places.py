from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_places_returns_sample_records():
    response = client.get("/places")

    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_filter_places_by_city():
    response = client.get("/places", params={"city": "Ames"})

    assert response.status_code == 200
    assert all(
        place["city"] == "Ames"
        for place in response.json()
    )


def test_filter_places_by_category():
    response = client.get(
        "/places",
        params={"category": "coffee"},
    )

    assert response.status_code == 200
    assert all(
        place["category"] == "coffee"
        for place in response.json()
    )


def test_invalid_category_is_rejected():
    response = client.get(
        "/places",
        params={"category": "nightlife"},
    )

    assert response.status_code == 422


def test_latitude_and_longitude_must_be_paired():
    response = client.get(
        "/places",
        params={"lat": 42.03},
    )

    assert response.status_code == 422


def test_radius_requires_coordinates():
    response = client.get(
        "/places",
        params={"radius_km": 5},
    )

    assert response.status_code == 422


def test_nearby_search_returns_places_within_radius():
    response = client.get(
        "/places",
        params={
            "lat": 42.03,
            "lon": -93.62,
            "radius_km": 5,
        },
    )

    assert response.status_code == 200
    assert all(
        (
            (place["latitude"] - 42.03) ** 2
            + (place["longitude"] + 93.62) ** 2
        ) < 1
        for place in response.json()
    )
