from bytes_app import get_headlines, get_summary
from rich.console import Console
from rich.table import Table
from rich import print
from rich.panel import Panel


def headlines_table():
    table = Table(title="News_Bytes", show_lines=True)

    table.add_column("Headlines", justify="center", style="magenta")

    for headline in get_headlines():
        table.add_row(headline[0])
    return table


headlines_table()


# TOTO: layout to panel completion
def categories_panel():
    print(Panel.fit("[green]News!"))
    print(Panel.fit("[green]Business!"))
    print(Panel.fit("[green]World News!"))
    print(Panel.fit("[green]Tech!"))
    print(Panel.fit("[green]Sports!"))

    # table.add_column("News", justify="center", style="green", no_wrap=True)
    # table.add_column("Business", justify="center", style="green")
    # table.add_column("World News", justify="center", style="green")
    # table.add_column("Tech", justify="center", style="green")
    # table.add_column("Sports", justify="center", style="green")


# TODO:
# table.add_row("input()")

console = Console()
console.print(headlines_table())
categories_panel()
