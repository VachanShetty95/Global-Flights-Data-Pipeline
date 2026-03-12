"""
Data ingestion components for reading files from disk.
"""

import logging
import pandas as pd
from typing import Optional
from pathlib import Path

logger = logging.getLogger("etl.ingestion")


class CSVReader:
    """Class responsible for reading CSV data."""

    def __init__(self, data_dir: str):
        """
        Initialize the CSV reader.

        Args:
            data_dir: The directory containing the source CSV files.
        """
        self.data_dir = Path(data_dir)

    def read_csv(self, filename: str) -> pd.DataFrame:
        """
        Read a CSV file and perform standard cleaning.

        Args:
            filename: The name of the file to read relative to data_dir.

        Returns:
            A pandas DataFrame with the raw data.
            
        Raises:
            FileNotFoundError: If the CSV file does not exist.
        """
        file_path = self.data_dir / filename
        if not file_path.exists():
            logger.error(f"File not found: {file_path}")
            raise FileNotFoundError(f"Missing required dataset: {file_path}")

        logger.info(f"Loading data from {file_path}")
        df = pd.read_csv(file_path)

        # Standard cleaning
        if "Unnamed: 0" in df.columns:
            logger.debug("Dropping Unnamed: 0 column")
            df = df.drop(columns=["Unnamed: 0"])

        logger.info(f"Loaded {len(df)} rows from {filename}")
        return df
