from dagster import asset, RetryPolicy
import subprocess

@asset(
    description="Raw flights data ingested into PostgreSQL from CSV.",
    retry_policy=RetryPolicy(max_retries=3, delay=60)
)
def raw_flights_ingestion() -> None:
    """Run the Python ETL CLI to ingest flights data."""
    # Running the CLI we built in etl package
    # We assume 'etl' module is in PYTHONPATH. In Docker this will be handled.
    # For now, we can run it using python -m
    result = subprocess.run(["python", "-m", "etl.cli.main", "--sample", "True"], capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Ingestion failed: {result.stderr}")
