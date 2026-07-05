"""ETL Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_design_pipeline():
    """Test Design an ETL/ELT pipeline from source to destination."""
    tools = AgentTools()
    result = await tools.design_pipeline(source="test", destination="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_transformation():
    """Test Generate transformation code (dbt, Spark, SQL) from requirements."""
    tools = AgentTools()
    result = await tools.generate_transformation(description="test", source_schema="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_handle_schema_change():
    """Test Detect and handle schema evolution in data sources."""
    tools = AgentTools()
    result = await tools.handle_schema_change(source="test", previous_schema="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_monitor_pipeline():
    """Test Monitor pipeline health, data freshness, and throughput."""
    tools = AgentTools()
    result = await tools.monitor_pipeline(pipeline_id="test", metrics="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.etl_agent_agent import EtlAgentAgent
    agent = EtlAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
