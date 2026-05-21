# Snowflake Analytics Pipeline

A lightweight analytics pipeline built on Snowflake, designed for rapid metric computation and dashboard integration.

## Setup

```bash
pip install -r requirements.txt
cortex connections set analytics-prod
```

## Architecture

```
src/
├── extractors/     # Data source connectors
├── transforms/     # dbt-style transformations  
├── loaders/        # Snowflake stage → table loaders
└── metrics/        # Metric definitions (YAML)
```

## Usage

```bash
python src/run_pipeline.py --env prod --metrics daily_active_users
```

## Development

This project includes Cortex Code skills for project-specific guidance. Run `cortex` in this directory to get context-aware help.

## License

MIT
