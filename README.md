# IRIS Pilot Service - Portable Dockerized Pilot Runtime

## Prerequisites
- Docker
- Docker Compose

## Setup
1. Copy `.env.example` to `.env`

## Commands
- To run the application: `docker compose --profile app up --build`
- To run the smoke tests: `docker compose --profile test up smoke_test --build`

## Architecture Choices
- OOP with interfaces used via `SiteRepositoryInterface`.
- SQLAlchemy ORM for database interactions.
- Pandas and GeoPandas for geometry/data transformations.
- Pytest for automated testing covering schema, database health, worker, and data insertion.

## Assumptions
- `country_code` is required. Invalid rows are dropped during Pandas validation.
- Missing `eco_points` are transformed into NULL.
- Random logic provided for evaluation (pass/fail).
- Source endpoint data is local.
