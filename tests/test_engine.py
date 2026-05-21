"""Tests for metric engine."""
import pytest
from src.metrics.engine import MetricDefinition, _build_query


def test_build_query_simple():
    metric = MetricDefinition(
        name="dau",
        source="events.page_views",
        aggregation="count_distinct(user_id)",
        window="1 day",
    )
    sql = _build_query(metric)
    assert "SELECT count_distinct(user_id) AS value" in sql
    assert "FROM events.page_views" in sql


def test_build_query_with_filters():
    metric = MetricDefinition(
        name="mobile_dau",
        source="events.page_views",
        aggregation="count_distinct(user_id)",
        window="1 day",
        filters={"platform": "mobile"},
    )
    sql = _build_query(metric)
    assert "WHERE platform = 'mobile'" in sql


def test_metric_definition():
    metric = MetricDefinition(
        name="test",
        source="db.schema.table",
        aggregation="count(*)",
        window="7 days",
    )
    assert metric.name == "test"
    assert metric.filters is None
