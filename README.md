# Snowflake Analytics Pipeline

A lightweight analytics pipeline built on Snowflake for automated metric computation, alerting, and dashboard integration.

## Features

- **Declarative metrics** — Define metrics in YAML, compute them automatically
- **Multi-environment** — Separate configs for dev/staging/prod
- **Snowflake-native** — Built on Snowflake SDK with warehouse-aware scheduling
- **Extensible** — Plugin architecture for custom extractors and transformations

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Set up Snowflake connection
export SNOWFLAKE_ACCOUNT=your_account
export SNOWFLAKE_USER=your_user
export SNOWFLAKE_PASSWORD=your_password

# Run metrics
python -m src.pipeline run --metrics daily_active_users --env dev
```

## Architecture

```
src/
├── pipeline.py         # CLI entry point
├── connection.py       # Snowflake connection management
└── metrics/
    ├── engine.py       # Metric computation engine
    └── definitions.yaml # Metric definitions

config/
├── dev.yaml           # Development environment config
└── prod.yaml          # Production environment config

tests/
└── test_engine.py     # Unit tests
```

## Metric Definitions

Metrics are defined in `src/metrics/definitions.yaml`:

```yaml
metrics:
  daily_active_users:
    source: events.page_views
    aggregation: count_distinct(user_id)
    window: 1 day
```

## Development

```bash
# Run tests
pytest tests/

# Check pipeline status
python -m src.pipeline status --env dev
```

## Cortex Code Integration

This project includes Cortex Code skills for enhanced development workflows. When using Cortex Code in this directory, you'll get project-aware assistance for:

- Writing and debugging metric definitions
- Snowflake query optimization
- Pipeline configuration

## License

Apache 2.0
