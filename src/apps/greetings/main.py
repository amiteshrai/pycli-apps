# src/apps/greetings/main.py

import click


@click.command()
@click.argument("first_name", type=click.STRING, default="Stranger")
@click.argument("last_name", type=click.STRING, default="")
def hello(first_name: str, last_name: str):
    """Greet the user with a nice formatted message"""
    if first_name != "Stranger":
        click.echo(f"Hello {first_name} {last_name}!")
    else:
        click.echo(f"Hello {first_name}!")
