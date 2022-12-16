from bytes_app import get_headlines, get_summary
from rich.console import Console
from rich.table import Table
from rich import print
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn
from rich.progress import track
from rich.theme import Theme
import time
from rich.columns import Columns
import pyfiglet
from rich import box




class Menu:
    def __init__(self):
        self.console = Console()


    def ascii_art(self):
        self.console.print(pyfiglet.figlet_format("WELCOME TO NEWS BYTES", font="slant", width=200), justify="center")

    # @staticmethod
    def progress_bar():
        with Progress() as progress:
            task = progress.add_task("Get headlines", total=10)
            for index, headline in enumerate(get_headlines()):
                progress.console.print(f"Populating Headlines: {index}")
                time.sleep(0.2)
            while not progress.finished:
                progress.update(task, advance=0.9)

    def headlines_table(self):
        table = Table(show_lines=True, row_styles=["dim", ""], title_justify="center", box=box.HEAVY_EDGE, highlight=True)

        table.add_column("Headlines", justify="center", style="light_steel_blue", header_style="light_sky_blue1")

        for index, headline in enumerate(get_headlines()):
            table.add_row(headline[0])
        self.console.print(table, justify="center")

    def categories_panel(self):
        news_list:list[str] = ['[magenta]Business', '[blue]World News', '[magenta]Tech', '[blue]Sports']
        categories = [Panel(category, expand=True, box=box.HEAVY_EDGE) for category in news_list]
        self.console.print(Columns(categories), justify="center")

    def query_user(self):
        self.console.print(Panel('Enter a [red]category [white]if you wish to see more headlines,\n otherwise enter in a headline number in order to get a summary \n with a link to the article. If you wish to quit, enter (q)uit'), justify="center", style='Bold')

    def get_user_input(self):
        news = ['news', 'business', 'world news', 'tech', 'sports']
        user_input = input('> ')
        while user_input.lower() != 'q' or user_input.lower() != 'quit':
            if user_input in self.get_headlines().lower():
                #TODO: When the user specifies a headline we return that specific article
                pass
            elif user_input.lower() in news:
                #TODO: When the user specifies a category we return a new list of articles in that category
                pass
            elif user_input.lower() == 'r' or user_input.lower() == 'return':
                #TODO Returns user to a previous menu or state
                pass

    def display_category_news(self, category:str, headlines: list[str] = get_headlines()):
        table = Table(show_lines=True, row_styles=["cyan", "magenta"], title_justify="center", box=box.HEAVY_EDGE, highlight=True)

        table.add_column("#", justify="center")
        table.add_column(f'{category} news', justify="center")

        for index, headline in enumerate(headlines):
            table.add_row(str(index + 1), headline[0])

        self.console.print(table, justify="center")



menu = Menu()
# menu.ascii_art()
# # menu.progress_bar()
# menu.headlines_table()
# menu.categories_panel()
# menu.query_user()
# menu.get_user_input()
menu.display_category_news('Business')