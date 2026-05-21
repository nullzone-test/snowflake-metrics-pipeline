"""Snowflake connection management."""
import os
from pathlib import Path


def get_connection(env: str = "dev"):
    """Get Snowflake connection for the specified environment."""
    try:
        from snowflake.connector import connect
    except ImportError:
        raise RuntimeError("snowflake-connector-python not installed. Run: pip install -r requirements.txt")
    
    config = _load_connection_config(env)
    return connect(**config)


def _load_connection_config(env: str) -> dict:
    """Load connection parameters from environment or config."""
    return {
        "account": os.environ.get("SNOWFLAKE_ACCOUNT", ""),
        "user": os.environ.get("SNOWFLAKE_USER", ""),
        "password": os.environ.get("SNOWFLAKE_PASSWORD", ""),
        "warehouse": os.environ.get("SNOWFLAKE_WAREHOUSE", "COMPUTE_WH"),
        "database": os.environ.get("SNOWFLAKE_DATABASE", "ANALYTICS"),
        "schema": os.environ.get("SNOWFLAKE_SCHEMA", "PUBLIC"),
    }
