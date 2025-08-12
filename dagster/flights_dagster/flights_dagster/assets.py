
# flights_dagster/assets.py
from dagster import Definitions
from dagster_dbt import dbt_assets
from pathlib import Path

# Path to the dbt project directory relative to the current file
dbt_project_dir = Path(__file__).parent.parent.parent.parent / "dbt" / "flights_dbt"
manifest_path = dbt_project_dir / "target" / "manifest.json"

@dbt_assets(manifest=manifest_path)
def dbt_assets():
    """Load dbt assets from the manifest file."""
    pass

__all__ = ["dbt_assets"]
