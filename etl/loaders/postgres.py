"""
Data loading components for PostgreSQL.
"""

import logging
import pandas as pd
from sqlalchemy import create_engine, Engine
from sqlalchemy.exc import SQLAlchemyError

logger = logging.getLogger("etl.loaders")


class PostgresLoader:
    """Class responsible for loading pandas DataFrames into PostgreSQL."""

    def __init__(self, database_url: str):
        """
        Initialize the PostgresLoader.

        Args:
            database_url: The SQLAlchemy connection string.
        """
        # Hiding passwords in logs
        safe_url = database_url.split('@')[-1] if '@' in database_url else "database"
        logger.debug(f"Initializing engine for {safe_url}")
        self.engine: Engine = create_engine(database_url)

    def load_dataframe(self, df: pd.DataFrame, table_name: str, if_exists: str = "replace") -> None:
        """
        Load a DataFrame into a PostgreSQL table.

        Args:
            df: The pandas DataFrame to insert.
            table_name: The destination table name.
            if_exists: The strategy to use if table exists ('replace', 'append', 'fail').

        Raises:
            SQLAlchemyError: If a database error occurs.
        """
        logger.info(f"Writing {len(df)} rows to table '{table_name}' with mode '{if_exists}'")
        try:
            df.to_sql(table_name, con=self.engine, if_exists=if_exists, index=False)
            logger.info(f"Successfully loaded {table_name}")
        except SQLAlchemyError as e:
            logger.error(f"Failed to load table {table_name}: {e}")
            raise
