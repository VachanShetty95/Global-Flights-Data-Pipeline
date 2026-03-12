# ✈️ Global Flights Data Platform

A production-grade, open-source data engineering platform built using the Kaggle US Flight Delays 2015 dataset. 

This repository demonstrates modern best practices across data ingestion, transformation, orchestration, and observability.

## 🏗️ Architecture Stack

- **Data Source**: CSV files (Kaggle Flights Data 100k Sample)
- **Ingestion**: Python (pandas, Typer, Pydantic, SQLAlchemy)
- **Data Warehouse**: PostgreSQL
- **Transformation**: dbt (Data Build Tool)
- **Orchestration**: Dagster 
- **Observability**: Prometheus, Node Exporter, Postgres Exporter
- **Monitoring & Alerting**: Grafana
- **BI/Analytics Layer**: Metabase

## 📂 Project Structure

```text
.
├── dagster/            # Dagster definitions (assets, jobs, schedules)
├── datasets/           # Source CSV data
├── dbt/                # dbt project and tests
├── docker/             # Unified docker-compose.yml
├── etl/                # Modular Python ingestion pipeline
├── monitoring/         # Prometheus + Grafana provisioning and dashboards
└── tests/              # Pytest modules (unit, integration, observability)
```

## 🚀 Quick Start (Running the Platform)

1. **Environment Setup**:
   Copy the environment variables template.
   ```bash
   cp .env.template .env
   ```

2. **Spin Up Infrastructure**:
   Launch all services via Docker Compose.
   ```bash
   cd docker
   docker compose up -d
   ```

3. **Orchestrate Pipelines**:
   - Access the Dagster UI at `http://localhost:3002`.
   - Materialize the `raw_flights_ingestion` asset followed by the `dbt_models` asset.

4. **Monitoring & Alerting**:
   - Access Grafana at `http://localhost:3000` (User: `admin` / Password: `admin`).
   - Navigate to the provisioned dashboards for System Health and Pipeline Monitoring.

5. **Analytics**:
   - Access Metabase at `http://localhost:3001` and connect it to `postgres:5432` using credentials in `.env`.

## 🧪 Testing

We utilize Pytest and dbt tests for strict governance.
- Run Python tests: `pytest tests/`
- Run dbt tests: `dbt test --project-dir dbt/flights_dbt`