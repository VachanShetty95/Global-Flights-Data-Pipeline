# Changelog

All notable changes to the Global Flights Data Platform will be documented in this file.

## [Unreleased] - 2026-03-11

### Added
- **Environment Management**: Added `.env.template` and `.env` standard for configuration management.
- **Python ETL Modularization**: Refactored `etl/load_to_postgres.py` into `etl/ingestion`, `etl/loaders`, and `etl/config` with strict typing and structured logging.
- **CLI Entrypoint**: Added Typer CLI for triggering the ETL Python jobs.
- **End-to-End Testing**: Added pytest configurations for ingestion, loading, and dashboard JSON schema validations. Added dbt tests across dimensional models.
- **Dagster Orchestration**: Defined Python assets (`raw_flights_ingestion`, `dbt_models`), daily and backfill jobs, and cron-based schedules (`0 3 * * *`).
- **Unified Docker Platform**: Created a central `docker-compose.yml` to spin up Postgres, Dagster, Prometheus, Node Exporter, Postgres Exporter, Grafana, and Metabase.
- **Observability Stack**: Added `prometheus.yml` definitions to scrape performance metrics. Created basic System and Pipeline Monitoring dashboards for Grafana using Provisioning APIs. Add Prometheus alerting rules for DB anomalies and pipeline failures.
- **Documentation**: Overhauled `README.md` to explain architecture, execution steps, and monitoring stack details.

### Changed
- Refactored project directory structure into a standard Clean Architecture format (`etl/`, `dbt/`, `dagster/`, `monitoring/`, `docker/`, `tests/`).
- `requirements.txt` updated to include `pydantic`, `typer`, `dagster`, and `pytest`.

### Removed
- Removed the monolithic unstructured script `etl/load_to_postgres.py`.
