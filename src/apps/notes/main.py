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


@click.group()
@click.pass_context
def main(ctx):
    """
    Manage your notes

    _extended_summary_
    """
    ctx.ensure_object(dict)
    ctx.obj["notes"] = load_notes()


def load_notes():
    notes_db = "notes.txt"
    notes = []
    with open(notes_db, "r") as f:
        for line in f:
            notes.append(line.strip())

    return "\n".join(notes)


@main.command()
@click.pass_context
def show(ctx):
    """
    show notes

    _extended_summary_
    """
    click.echo("Displaying notes...")
    # Actually show the notes by implementing the logic below

    click.echo(ctx.obj["notes"])


@main.command()
def add():
    """
    add notes

    _extended_summary_
    """


@main.command()
def update():
    """
    update notes

    _extended_summary_
    """


@main.command()
@click.pass_context
def delete(ctx):
    """
    delete notes

    _extended_summary_
    """

    notes = ctx.obj["notes"]
    click.echo("Displaying notes...")
    click.echo(notes)

    idx = click.prompt(
        "Enter the index of the note to be deleted OR -1 to exit", type=click.INT
    )
    if idx == -1:
        return
    idx -= 1
    notes_arr = notes.splitlines()
    click.echo(f"Removing note at index {idx+1} which is:\n{notes_arr[idx]}")
    notes_arr.remove(notes_arr[idx])
