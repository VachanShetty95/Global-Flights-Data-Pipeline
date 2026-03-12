from dagster import define_asset_job

daily_pipeline_job = define_asset_job(
    name="daily_pipeline",
    selection=["raw_flights_ingestion", "dbt_models", "analytics_models"]
)

backfill_pipeline_job = define_asset_job(
    name="backfill_pipeline",
    selection=["raw_flights_ingestion", "dbt_models"]
)
