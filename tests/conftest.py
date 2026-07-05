"""Test configuration for ETL Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "etl-agent", "category": "Data Engineering"}
