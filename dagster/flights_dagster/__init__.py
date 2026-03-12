from dagster import Definitions, load_assets_from_modules

from flights_dagster.assets import ingestion, dbt
from flights_dagster.jobs import daily_pipeline_job, backfill_pipeline_job
from flights_dagster.schedules import daily_pipeline_schedule

all_assets = load_assets_from_modules([ingestion, dbt])

defs = Definitions(
    assets=all_assets,
    jobs=[daily_pipeline_job, backfill_pipeline_job],
    schedules=[daily_pipeline_schedule],
)
