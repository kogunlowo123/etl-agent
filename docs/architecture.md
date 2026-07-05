# ETL Agent Architecture

Extract-Transform-Load pipeline agent that designs data pipelines, generates transformation logic, monitors pipeline health, handles schema evolution, and orchestrates batch and streaming data workflows.

## Domain Tools

- **design_pipeline**: Design an ETL/ELT pipeline from source to destination
- **generate_transformation**: Generate transformation code (dbt, Spark, SQL) from requirements
- **handle_schema_change**: Detect and handle schema evolution in data sources
- **monitor_pipeline**: Monitor pipeline health, data freshness, and throughput
- **debug_pipeline_failure**: Diagnose and suggest fixes for pipeline failures