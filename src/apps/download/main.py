# src/apps/download/main.py

import click
import requests


@click.command()
@click.argument("urls", nargs=-1)
def download(urls):
    """
    Download resources from the given URLs and save it to the given file
    Example:
        > download https://wiki.com/some-article.txt,some-article.txt
        This will fetch the article and save it to some-article.txt file.
    """

    # Crteate a context manager with progressbar
    # with click.progressbar(urls) as bars:
    #     for item in bars:
    #         url, filename = item.split(",")
    #         response = requests.get(url)
    #         with open(filename, "w") as f:
    #             f.write(response.text)

    # Another way to show the progressbar with more info
    with click.progressbar(
        length=len(urls),
        show_eta=False,
        item_show_func=(lambda name: f"Downloading {name}"),
    ) as bar:
        for i, item in enumerate(urls):
            url, filename = item.split(",")
            response = requests.get(url)
            with open(filename, "w") as f:
                f.write(response.text)
            bar.update(i, filename)
