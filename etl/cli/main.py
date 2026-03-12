"""
Command Line Interface for the ETL pipeline.
Uses Typer for clean CLI definition and dependencies for robust execution.
"""

import typer
import logging
from typing import Optional

from etl.config.settings import get_postgres_settings, get_app_settings
from etl.logging.setup import setup_logging
from etl.ingestion.reader import CSVReader
from etl.loaders.postgres import PostgresLoader

app = typer.Typer(help="Global Flights ETL Pipeline CLI")

@app.command()
def load_data(
    sample: bool = typer.Option(True, help="Load the sample dataset instead of full"),
    log_level: str = typer.Option("INFO", help="Logging level (DEBUG, INFO, WARNING, ERROR)")
):
    """
    Run the ETL pipeline to load data from CSV files into PostgreSQL.
    """
    # Setup logging
    level = getattr(logging, log_level.upper(), logging.INFO)
    logger = setup_logging(level)
    
    logger.info("Starting ETL pipeline")

    try:
        # Load configuration
        pg_settings = get_postgres_settings()
        app_settings = get_app_settings()

        # Initialize components via dependency injection
        reader = CSVReader(data_dir=app_settings.datasets_dir)
        loader = PostgresLoader(database_url=pg_settings.database_url)

        # Datasets to load
        # We assume flights_sample.csv exists if sample=True, otherwise flights.csv
        flights_file = "flights_sample.csv" if sample else "flights.csv"
        datasets = [
            {"filename": flights_file, "table": "flights_raw"},
            {"filename": "airports.csv", "table": "airports"},
            {"filename": "airlines.csv", "table": "airlines"}
        ]

        # Execute Pipeline
        for dataset in datasets:
            try:
                df = reader.read_csv(dataset["filename"])
                loader.load_dataframe(df, table_name=dataset["table"], if_exists="replace")
            except FileNotFoundError as e:
                logger.warning(f"Skipping {dataset['filename']}: {e}")
            except Exception as e:
                logger.error(f"Failed processing {dataset['filename']}: {e}")
                raise typer.Exit(code=1)

        logger.info("ETL pipeline completed successfully")

    except Exception as e:
        logger.exception("An unexpected error occurred during the ETL process.")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
