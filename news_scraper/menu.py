from rich.console import Console
from rich.table import Table
from rich import print
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn
from rich.progress import track
from rich.theme import Theme
import time
from rich import inspect
from rich.columns import Columns
from rich.table import Column
from rich.prompt import Prompt, Confirm
import pyfiglet
import sys
from rich import box

import bbc

bbc = bbc.BBC()


class Menu:
    def __init__(self):
        self.console = Console()


    def ascii_art(self):
        self.console.print(pyfiglet.figlet_format("WELCOME TO\n NEWS BYTES", font="slant", width=200), justify="center")

    @staticmethod
    def progress_bar(lst:list):
        for _ in track(lst, description="[green], fetching articles"):
            time.sleep(0.02)


    def make_headlines_table(self, headlines:list[str] = bbc.get_news_headlines()):
        table = Table(show_lines=True, row_styles=["cyan", "magenta"], title_justify="center", box=box.HEAVY_EDGE, highlight=True)

        table.add_column("#", justify="center")
        table.add_column("[i]Headlines", justify="center", style="light_steel_blue", header_style="light_sky_blue1")

        for index, headline in enumerate(headlines):
            table.add_row(str(index + 1),headline[0])
        self.console.print(table, justify="center")

    @staticmethod
    def check_index(number:int, numbers_list:list[int]):
        if number in numbers_list:
            return numbers_list.index(number)
        return False

    def categories_panel(self):
        news_list:list[str] = ['[magenta]Business', '[blue]World News', '[magenta]Tech', '[blue]Sports']
        categories = [Panel(category, expand=True, box=box.HEAVY_EDGE) for category in news_list]
        self.console.print(Columns(categories), justify="center")

    def query_user(self):
        self.console.print(Panel('Enter a [red]category [white]if you wish to see more headlines,\n otherwise enter in a headline number in order to get a summary \n with a link to the article. If you wish to quit, enter (q)uit'), justify="center", style='Bold')

    @staticmethod
    def get_user_input():
        while True:
            user_input = Prompt.ask("Select a category", choices=['Business', 'World News', 'Tech', 'Sports'])
            if user_input.lower() == 'q' or user_input.lower() == 'quit':
                if Confirm.ask("Are you sure you would like to quit?"):
                    sys.exit()
            # elif user_input in temp_list:
            #     #TODO display category headlines or text
            #     pass



    def display_category_news(self, category:str, headlines: list[str] = bbc.get_news_headlines()):
        table = Table(show_lines=True, row_styles=["cyan", "magenta"], title_justify="center", box=box.HEAVY_EDGE, highlight=True)

        table.add_column("#", justify="center")
        table.add_column(f'{category} news_scraper', justify="center")

        for index, headline in enumerate(headlines):
            table.add_row(str(index + 1), headline[0])

        self.console.print(table, justify="center")


    def display_article_summary(self,headline: tuple = bbc.get_news_headlines()):
        #TODO Change headlines to whatever response is
        # if user_input in headlines:
        #     self.console.print(f'[u]{Panel(get_summary(headline[0][1]))}', justify="center")
        self.console.print(Panel(bbc.get_news_headlines()[0][1]), Panel(bbc.get_news_headlines()[0][1]), justify="center")
        self.console.print(f'Input (r)eturn to return to the main menu or type (q) to quit', justify="center")



# inspect('', methods=True)
# inspect(Panel, methods=True)
menu = Menu()
# menu.display_article_summary('Hello')
# menu.ascii_art()
# # menu.progress_bar()
menu.make_headlines_table()
# menu.categories_panel()
# menu.query_user()
# menu.get_user_input()
# menu.display_category_news('Business')