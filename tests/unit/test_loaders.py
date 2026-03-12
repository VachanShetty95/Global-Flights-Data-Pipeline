import pytest
import pandas as pd
from unittest.mock import MagicMock, patch
from etl.loaders.postgres import PostgresLoader
from sqlalchemy.exc import SQLAlchemyError

@patch("etl.loaders.postgres.create_engine")
def test_postgres_loader_success(mock_create_engine):
    """Test successful data loading to Postgres."""
    mock_engine = MagicMock()
    mock_create_engine.return_value = mock_engine
    
    loader = PostgresLoader("sqlite:///:memory:")
    
    df = pd.DataFrame({"id": [1], "name": ["test"]})
    df.to_sql = MagicMock()
    
    loader.load_dataframe(df, "test_table")
    df.to_sql.assert_called_once_with("test_table", con=mock_engine, if_exists="replace", index=False)

@patch("etl.loaders.postgres.create_engine")
def test_postgres_loader_failure(mock_create_engine):
    """Test PostgresLoader raises exception on db failure."""
    mock_engine = MagicMock()
    mock_create_engine.return_value = mock_engine
    
    loader = PostgresLoader("sqlite:///:memory:")
    
    df = pd.DataFrame({"id": [1], "name": ["test"]})
    df.to_sql = MagicMock(side_effect=SQLAlchemyError("DB Error"))
    
    with pytest.raises(SQLAlchemyError):
        loader.load_dataframe(df, "test_table")
