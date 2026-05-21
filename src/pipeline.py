"""Snowflake Analytics Pipeline - Main entry point."""
import click
import yaml
from pathlib import Path


@click.group()
@click.option("--env", default="dev", help="Environment (dev/staging/prod)")
@click.pass_context
def cli(ctx, env):
    """Snowflake Analytics Pipeline CLI."""
    ctx.ensure_object(dict)
    ctx.obj["env"] = env


@click.command()
@click.option("--metrics", "-m", multiple=True, help="Metrics to compute")
@click.option("--warehouse", "-w", default="COMPUTE_WH", help="Snowflake warehouse")
@click.pass_context
def run(ctx, metrics, warehouse):
    """Run the analytics pipeline for specified metrics."""
    env = ctx.obj["env"]
    config = _load_config(env)
    
    click.echo(f"Running pipeline in {env} environment")
    click.echo(f"Warehouse: {warehouse}")
    click.echo(f"Metrics: {', '.join(metrics) if metrics else 'all'}")
    
    for metric in metrics or config.get("default_metrics", []):
        click.echo(f"  Computing: {metric}")


@click.command()
@click.pass_context
def status(ctx):
    """Show pipeline status and last run info."""
    env = ctx.obj["env"]
    click.echo(f"Pipeline status for {env}:")
    click.echo("  Last run: N/A")
    click.echo("  Status: idle")


def _load_config(env):
    """Load environment-specific configuration."""
    config_path = Path(__file__).parent.parent / "config" / f"{env}.yaml"
    if config_path.exists():
        with open(config_path) as f:
            return yaml.safe_load(f)
    return {}


cli.add_command(run)
cli.add_command(status)

if __name__ == "__main__":
    cli()
