from dagster import ScheduleDefinition
from flights_dagster.jobs import daily_pipeline_job

daily_pipeline_schedule = ScheduleDefinition(
    job=daily_pipeline_job,
    cron_schedule="0 3 * * *",
    execution_timezone="UTC"
)
