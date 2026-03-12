from dagster import asset, RetryPolicy
import subprocess
import os

@asset(
    description="dbt models transforming raw flights data into a star schema.",
    deps=["raw_flights_ingestion"],
    retry_policy=RetryPolicy(max_retries=2, delay=120)
)
def dbt_models() -> None:
    """Run dbt build to transform and test the data."""
    dbt_dir = os.environ.get("DBT_PROFILES_DIR", "/usr/src/app/dbt/flights_dbt")
    result = subprocess.run(["dbt", "build", "--project-dir", dbt_dir, "--profiles-dir", dbt_dir], capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"dbt build failed: {result.stdout}\n{result.stderr}")

@asset(
    description="Analytics and BI aggregation models.",
    deps=["dbt_models"]
)
def analytics_models() -> None:
    """Placeholder for further BI aggregations or specific analytics models."""
    pass
