# src/apps/notebook/main.py


import typing

import click


@click.command()
@click.argument("filename", type=click.File("a"))
def take_notes(filename: typing.IO):
    """
    take_notes _summary_

    _extended_summary_

    Args:
        filename (typing.IO): _description_
    """
    click.echo("Enter notes to be added below and then press CTRL+C to exit.")
    try:
        while True:
            value = click.prompt("", prompt_suffix=">>")
            filename.write(f"{value}\n")
    except click.Abort:
        click.echo(f"\nOutput written to the file {filename.name}")


@click.command()
@click.argument("input-files", type=click.File("r"), nargs=2)
@click.argument("output-file", type=click.File("w"))
def concat_notes(input_files: typing.Collection[typing.IO], output_file: typing.IO):
    """
    concat_notes _summary_

    _extended_summary_

    Args:
        input_file (typing.Collection[typing.IO]): _description_
        output_file (typing.IO): _description_
    """

    for f in input_files:
        for line in f:
            output_file.write(line)
        click.echo(f"{f.name} written to {output_file.name}")
