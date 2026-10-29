# Vyoma Travel Discovery App

A location-based travel discovery application designed to help travelers explore local food, coffee, and drinks at their destinations.

## Project Overview

Travelers often spend considerable time searching across multiple platforms to find local foods, coffee shops, and drinks worth trying. Vyoma aims to simplify this discovery process by organizing place information and recommendations into a location-based experience.

The initial product will focus on searching by destination, filtering by category, and presenting relevant places using permitted data sources.

## Project Objectives

- Develop a location-based place discovery experience.
- Organize places by category and geographic location.
- Evaluate permitted data sources for place and recommendation information.
- Design a maintainable software architecture.
- Build and test an initial application prototype.

## Initial Technology Stack

| Component            | Proposed Technology         |
| -------------------- | --------------------------- |
| Backend              | Python and FastAPI          |
| Frontend             | HTML, CSS, JavaScript       |
| Data validation      | Pydantic                    |
| Initial data storage | Sample data for prototyping |
| Testing              | Pytest                      |
| Version control      | Git and GitHub              |
| Future database      | To be evaluated             |

These technologies are initial proposals and may change as the requirements evolve.

## Planned MVP Features

1. Search for places by city or destination.
2. Filter places by food, coffee, and drinks.
3. Support geographic search using coordinates.
4. Display place details and available source information.
5. Integrate permitted external data sources after evaluating their terms.
6. Provide a foundation for future recommendation ranking.

## Repository Structure

```text
travel-discovery-app/
├── README.md
├── docs/
│   ├── requirements.md
│   ├── user-stories.md
│   ├── mvp-scope.md
│   ├── architecture.md
│   ├── data-model.md
│   ├── data-source-evaluation.md
│   └── work-log.md
├── backend/
├── frontend/
├── tests/
└── .gitignore
```

This structure represents the proposed organization of the project. Directories and implementation files will be added as development progresses.

## Development Roadmap

### Phase 1: Requirements and Design

- Analyze the user problem.
- Define functional and non-functional requirements.
- Design the initial architecture.
- Develop the data model.
- Evaluate possible data sources.

### Phase 2: Prototype Development

- Initialize the backend.
- Implement the initial search API.
- Develop category and geographic filtering.
- Build a basic user interface.
- Add automated tests.

### Phase 3: Data Integration

- Select an appropriate permitted data provider.
- Implement data ingestion and validation.
- Evaluate persistent database options.
- Improve data quality and error handling.

### Phase 4: Recommendation and User Experience

- Explore ranking approaches.
- Improve search relevance.
- Design place-detail and saved-place experiences.
- Evaluate performance and usability.

## Data Usage Principles

The application will use external data only after reviewing applicable terms, permissions, attribution requirements, storage restrictions, and commercial-use conditions.

Social-media content will not be scraped or stored unless the applicable permissions and terms allow the intended use.

## Current Status

Initial planning and design.

Features should be marked as implemented only after they have been developed and tested.

## Work Documentation

Technical decisions, design changes, implementation progress, test results, and actual work hours will be documented throughout development.

See `docs/work-log.md` for the daily work-log template.
