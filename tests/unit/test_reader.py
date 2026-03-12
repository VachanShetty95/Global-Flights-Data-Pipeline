import pytest
import pandas as pd
from pathlib import Path
from etl.ingestion.reader import CSVReader

def test_read_csv_success(tmp_path: Path):
    """Test reading a valid CSV file."""
    df_data = pd.DataFrame({"col1": [1, 2], "Unnamed: 0": [0, 1]})
    file_path = tmp_path / "valid.csv"
    df_data.to_csv(file_path, index=False)
    
    reader = CSVReader(data_dir=str(tmp_path))
    df = reader.read_csv("valid.csv")
    
    assert len(df) == 2
    assert "col1" in df.columns
    assert "Unnamed: 0" not in df.columns

def test_read_csv_not_found():
    """Test reading a missing CSV file raises FileNotFoundError."""
    reader = CSVReader(data_dir="/tmp/nonexistent")
    with pytest.raises(FileNotFoundError):
        reader.read_csv("missing.csv")
