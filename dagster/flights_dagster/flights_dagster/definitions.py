# flights_dagster/definitions.py
from dagster import Definitions
from flights_dagster.assets import dbt_assets

defs = Definitions(
    assets=[dbt_assets],
)
