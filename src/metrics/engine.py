"""Metric computation engine."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class MetricDefinition:
    name: str
    source: str
    aggregation: str
    window: str
    filters: Optional[dict] = None


def load_metrics(path: str) -> list[MetricDefinition]:
    """Load metric definitions from YAML."""
    import yaml
    with open(path) as f:
        data = yaml.safe_load(f)
    
    metrics = []
    for name, config in data.get("metrics", {}).items():
        metrics.append(MetricDefinition(
            name=name,
            source=config["source"],
            aggregation=config["aggregation"],
            window=config["window"],
            filters=config.get("filters"),
        ))
    return metrics


def compute_metric(metric: MetricDefinition, connection) -> dict:
    """Compute a single metric against Snowflake."""
    sql = _build_query(metric)
    result = connection.execute(sql)
    return {"metric": metric.name, "value": result, "window": metric.window}


def _build_query(metric: MetricDefinition) -> str:
    """Build SQL query from metric definition."""
    base = f"SELECT {metric.aggregation} AS value FROM {metric.source}"
    if metric.filters:
        conditions = " AND ".join(
            f"{k} = '{v}'" for k, v in metric.filters.items()
        )
        base += f" WHERE {conditions}"
    return base
