# src/apps/greetings/main.py

import click


@click.command()
@click.argument("first-name", type=click.STRING, default="Stranger")
@click.argument("last-name", type=click.STRING, default="")
@click.option(
    "--lang",
    default="en",
    type=click.Choice(["en", "es"]),
    help="Language in which the greetings will be displayed. Default is english(en) with spanish(es) as another option.",
)
def hello(first_name: str, last_name: str, lang: str):
    """Greet the user with a nice formatted message"""

    message = "Hello" if lang == "en" else "Hola"
    message = f"{message} {first_name} {last_name}!"
    if first_name != "Stranger":
        if lang == "es":
            click.echo(message)
        elif lang == "en":
            click.echo(message)
        else:
            raise click.BadOptionUsage(
                "lang",
                f"Unsupported language '{lang}'. Valid options are either 'en' or 'es'",
            )
    else:
        click.echo(f"Hello {first_name}!")
