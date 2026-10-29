# API Design: Travel Discovery Application

## 1. Purpose

Define the initial API contract for the location-based travel discovery application. This document describes the planned endpoints, request parameters, response structures, and validation behavior.

## 2. Initial Endpoints

### `GET /health`

Checks whether the API is responding.

**Successful response:**

```json
{
  "status": "ok"
}
```

### `GET /places`

Returns place records and supports optional filtering.

**Supported query parameters:**

| Parameter   | Type   | Purpose                                             |
| ----------- | ------ | --------------------------------------------------- |
| `city`      | String | Filter by city                                      |
| `category`  | String | Filter by category, such as food, coffee, or drinks |
| `lat`       | Number | Latitude for nearby search                          |
| `lon`       | Number | Longitude for nearby search                         |
| `radius_km` | Number | Search radius in kilometers                         |

Nearby-search parameters should be validated. Latitude must be between -90 and 90, longitude between -180 and 180, and radius must be positive. The API should require latitude and longitude together.

**Example request:**

`GET /places?city=Ames&category=coffee`

**Illustrative response:**

```json
[
  {
    "id": 1,
    "name": "Sample Coffee Shop",
    "city": "Ames",
    "category": "coffee",
    "latitude": 42.03,
    "longitude": -93.62,
    "description": "Illustrative sample record",
    "source": "sample"
  }
]
```

The sample place above is fictional and is provided only to demonstrate the response structure.

## 3. Data and Error Handling

- Validate query parameters before performing a search.
- Return structured JSON responses.
- Use sample data for the initial prototype.
- Do not imply that sample records represent verified real businesses.
- Document invalid-input behavior and test it.
- Evaluate source permissions and attribution requirements before importing external place data.

## 4. Current Limitations

- Initial data may be held in memory.
- Results may be limited to sample records.
- No authentication or production deployment is defined in this initial prototype.
- A real external data source has not been selected by this document.

## 5. Future Enhancements

Potential enhancements include database persistence, pagination, map integration, saved places, recommendation ranking, and permitted external data integrations.
