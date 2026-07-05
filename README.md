# ETL Agent

[![CI](https://github.com/kogunlowo123/etl-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/etl-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Data Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Extract-Transform-Load pipeline agent that designs data pipelines, generates transformation logic, monitors pipeline health, handles schema evolution, and orchestrates batch and streaming data workflows.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `design_pipeline` | Design an ETL/ELT pipeline from source to destination |
| `generate_transformation` | Generate transformation code (dbt, Spark, SQL) from requirements |
| `handle_schema_change` | Detect and handle schema evolution in data sources |
| `monitor_pipeline` | Monitor pipeline health, data freshness, and throughput |
| `debug_pipeline_failure` | Diagnose and suggest fixes for pipeline failures |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/etl/design` | Design a pipeline |
| `POST` | `/api/v1/etl/transform` | Generate transformation |
| `POST` | `/api/v1/etl/schema-change` | Handle schema change |
| `GET` | `/api/v1/etl/monitor` | Monitor pipeline |
| `POST` | `/api/v1/etl/debug` | Debug pipeline failure |

## Features

- Pipeline Design
- Transformation Generation
- Schema Evolution
- Pipeline Monitoring
- Data Orchestration

## Integrations

- Apache Spark
- Dbt
- Airflow
- Fivetran
- Databricks

## Architecture

```
etl-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── etl_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Apache Spark + dbt + Airflow + Fivetran**

---

Built as part of the Enterprise AI Agent Platform.
