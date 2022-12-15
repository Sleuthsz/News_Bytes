from bytes_app import get_headlines, get_summary
from rich.console import Console
from rich.table import Table
from rich import print
from rich.panel import Panel
from rich.progress import track
from time import sleep
from rich.columns import Columns
from rich import box
import sys

console = Console()
def headlines_table():
    table = Table(show_lines=True, row_styles=["dim", ""], title_justify="center", box=box.HEAVY_EDGE)

    table.add_column("Headlines", justify="center", style="light_steel_blue", header_style="light_sky_blue1")

    for index, headline in enumerate(get_headlines()):
        table.add_row(headline[0])
    console.print(table, justify="center")

# TODO: layout to panel completion
def categories_panel():
    news = ['[blue]News', '[magenta]Business', '[blue]World News', '[magenta]Tech', '[blue]Sports']
    news_render = [Panel(category, expand=True) for category in news]
    console.print(Columns(news_render), justify="center")


def prompt_user():
    console.print('Enter a category if you wish to see more headlines,\n otherwise enter in a headline number in order to get a summary \n with a link to the article. If you wish to quit, enter (q)uit', justify="center")


def get_user_input():
    news = ['news', 'business', 'world news', 'tech', 'sports']
    user_input = input('> ')
    while user_input.lower() != 'q' or user_input.lower() != 'quit':
        if user_input in get_headlines().lower():
            #TODO: When the user specifies a headline we return that specific article
            pass
        elif user_input.lower() in news1:
            #TODO: When the user specifies a category we return a new list of articles in that category
            pass
        elif user_input.lower() == 'r' or user_input.lower() == 'return':
            #TODO Returns user to a previous menu or state
            pass



headlines_table()
categories_panel()
prompt_user()
