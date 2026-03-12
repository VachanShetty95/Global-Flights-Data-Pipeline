import pytest
import json
from pathlib import Path

DASHBOARD_DIR = Path("monitoring/grafana/dashboards")

def get_dashboards():
    """Returns a list of dashboard JSON files."""
    if not DASHBOARD_DIR.exists():
        return []
    return list(DASHBOARD_DIR.glob("*.json"))

@pytest.mark.parametrize("dashboard_file", get_dashboards())
def test_dashboard_is_valid_json(dashboard_file: Path):
    """Test that all dashboard files are valid JSON."""
    with dashboard_file.open("r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            assert isinstance(data, dict), "Dashboard JSON must be a dictionary at the root level."
            assert "uid" in data, "Dashboard must have a 'uid'."
            assert "title" in data, "Dashboard must have a 'title'."
            assert "panels" in data, "Dashboard must contain 'panels'."
        except json.JSONDecodeError as e:
            pytest.fail(f"Invalid JSON in {dashboard_file.name}: {e}")
