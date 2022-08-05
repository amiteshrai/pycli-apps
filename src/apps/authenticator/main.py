# src/apps/authenticator/main.py

import click


@click.command()
@click.option("--username", type=click.STRING, prompt=True, required=True)
@click.option(
    "--password", type=click.STRING, prompt=True, required=True, hide_input=True
)
def auth_options(username, password):
    """
    Authenticate user usign the given username and password.

    Args:
        username (text): The registered username
        password (text): The user's password'
    """

    click.echo(
        f"Authenticating user with username {username} and password hash {password}"
    )


@click.command()
def auth_prompt():
    """
    Authenticate user usign the given username and password.
    """
    username = click.prompt("username")
    password = click.prompt("password", hide_input=True, confirmation_prompt=True)
    otp = click.prompt("otp", type=click.INT)

    click.echo(
        f"Authenticating user with username {username} and password hash {id(password)}"
    )
    click.echo(f"Entered OTP is {otp}")

    is_admin = click.confirm("Are you logging in as admin?")
    if is_admin:
        admin_id = click.prompt("Admin ID", type=click.INT, prompt_suffix=">>")
        click.echo(f"Logging {username} as admin with admin ID {admin_id}")
    else:
        click.echo(f"Logging {username} as a regular user")
