# Initial Data Model

## 1. Purpose

This document defines the initial conceptual data model for the Vyoma Travel Discovery Application.

The model is intended to support place discovery, destination filtering, category filtering, and geographic search.

It is a proposed design and may change after data-source and database requirements are evaluated.

## 2. Place Entity

| Field       | Proposed Type       | Description                          |
| ----------- | ------------------- | ------------------------------------ |
| id          | String or UUID      | Unique identifier for a place record |
| name        | String              | Display name of the place            |
| category    | Enum/String         | Food, coffee, or drinks              |
| city        | String              | City associated with the place       |
| description | Text                | Available descriptive information    |
| latitude    | Decimal             | Geographic latitude                  |
| longitude   | Decimal             | Geographic longitude                 |
| source_id   | Optional identifier | Reference to the data source         |
| source_url  | Optional string     | Source URL when permitted            |
| created_at  | Timestamp           | Record creation time                 |
| updated_at  | Timestamp           | Last modification time               |

## 3. Category Values

Initial categories:

- food
- coffee
- drinks

The category model may be expanded if the product requires more granular classifications.

## 4. Source Entity

A separate source entity may be introduced when external data integration begins.

Potential fields:

- id
- provider_name
- official_documentation_url
- terms_url
- attribution_requirements
- permitted_usage_notes
- retention_restrictions
- date_reviewed

The model must not assume that a provider permits every proposed use.

## 5. Relationships

Proposed relationship:

- One source may provide multiple place records.
- Each place record may reference its source when known.
- A place may later be associated with multiple categories or recommendation records if requirements justify that complexity.

The final relationship structure will depend on the selected provider and database.

## 6. Data Validation

The application should validate:

- Required identifiers and names.
- Supported category values.
- Latitude between -90 and 90.
- Longitude between -180 and 180.
- Valid source URLs when provided.
- Duplicate identifiers.
- Missing or inconsistent data.

Additional normalization rules should be introduced based on actual data quality findings.

## 7. Geographic Search

The prototype may calculate approximate geographic distance between coordinates.

A production implementation should evaluate whether database-level geospatial indexing is appropriate for expected query volume and geographic search requirements.

## 8. Future Entities

Potential future entities include:

### Recommendation

- id
- place_id
- ranking_score
- ranking_method
- generated_at

### Saved Place

- id
- user_id
- place_id
- saved_at

These entities are outside the initial data-model commitment and should only be implemented when the relevant functionality is approved.

## 9. Open Design Questions

- Should categories be stored as an enum, lookup table, or normalized relationship?
- How should duplicate places from different sources be matched?
- Which source attribution details must be retained?
- How should stale records be identified?
- Is a dedicated geospatial database capability required?
- Which fields may be cached or stored under the selected provider's terms?
