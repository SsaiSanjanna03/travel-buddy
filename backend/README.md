# Travel Discovery API

## Overview

An initial FastAPI prototype for a location-based travel discovery application. The API supports place searches using sample data and optional city, category, and geographic-radius filters.

## Requirements

- Python 3.10 or newer
- pip

## Setup

From the repository root, create and activate a virtual environment:

```bash
python -m venv .venv
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r backend/requirements.txt
```

## Run the API

From the `backend` directory:

```bash
uvicorn app.main:app --reload
```

The API will normally be available at `http://127.0.0.1:8000`.

Interactive API documentation is available at `/docs`.

## Endpoints

- `GET /health`: Health check.
- `GET /places`: Search the sample place records.

Example:

```text
GET /places?city=Ames&category=coffee
```

Nearby-search example:

```text
GET /places?lat=42.03&lon=-93.62&radius_km=5
```

## Run Tests

From the repository root:

```bash
python -m pytest tests -v
```

If the test environment cannot import the `app` package from the repository root, run the tests with the backend directory on the Python path:

```bash
PYTHONPATH=backend python -m pytest tests -v
```

## Limitations

- The prototype uses fictional, in-memory sample records.
- Records are not verified real-world recommendations.
- Data is not persistent between application restarts.
- No external place-data provider is integrated.
- The prototype is not yet production-ready.
