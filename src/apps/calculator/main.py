# src/apps/calculator/main.py

import click


@click.command()
@click.argument("x", type=click.INT)
@click.argument("y", type=click.INT)
@click.option("-v", "--verbose", help="Show verbose output", default=True, is_flag=True)
def add(x: int, y: int, verbose: bool = True):
    """Adds numbers"""
    if verbose:
        click.echo(f"Adding numbers {x} and {y}")
    click.echo(f"Sum is: {x + y}")


@click.command()
@click.argument("x", type=click.INT)
@click.argument("y", type=click.INT)
@click.option("-v", "--verbose", help="Show verbose output", count=True)
def subtract(x: int, y: int, verbose: int):
    """Subtracts numbers"""
    click.echo(f"Verbosity is {verbose}")
    click.echo(f"Difference is: {x - y}")
