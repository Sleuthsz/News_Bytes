from bytes_app import get_headlines, get_summary
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
import pyfiglet
from rich import box




class Menu:
    def __init__(self):
        self.console = Console()


    def ascii_art(self):
        self.console.print(pyfiglet.figlet_format("WELCOME TO NEWS BYTES", font="slant", width=200), justify="center")

    @staticmethod
    def progress_bar(lst:list):
        text_column = TextColumn("{task.description}", table_column=Column(ratio=1))
        bar_column = BarColumn(bar_width=None, table_column=Column(ratio=2))
        progress = Progress(text_column, bar_column, expand=True)
        with progress:
            for _ in progress.track(lst):
                time.sleep(0.1)


    def make_headlines_table(self, headlines:list[str] = get_headlines()):
        table = Table(show_lines=True, row_styles=["cyan", "magenta"], title_justify="center", box=box.HEAVY_EDGE, highlight=True)

        table.add_column("#", justify="center")
        table.add_column("[i]Headlines", justify="center", style="light_steel_blue", header_style="light_sky_blue1")

        for index, headline in enumerate(headlines):
            table.add_row(str(index + 1),headline[0])
        self.console.print(table, justify="center")

    def categories_panel(self):
        news_list:list[str] = ['[magenta]Business', '[blue]World News', '[magenta]Tech', '[blue]Sports']
        categories = [Panel(category, expand=True, box=box.HEAVY_EDGE) for category in news_list]
        self.console.print(Columns(categories), justify="center")

    def query_user(self):
        self.console.print(Panel('Enter a [red]category [white]if you wish to see more headlines,\n otherwise enter in a headline number in order to get a summary \n with a link to the article. If you wish to quit, enter (q)uit'), justify="center", style='Bold')

    def get_user_input(self):
        news = ['business', 'world news', 'tech', 'sports']
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
                continue

    def display_category_news(self, category:str, headlines: list[str] = get_headlines()):
        table = Table(show_lines=True, row_styles=["cyan", "magenta"], title_justify="center", box=box.HEAVY_EDGE, highlight=True)

        table.add_column("#", justify="center")
        table.add_column(f'{category} news', justify="center")

        for index, headline in enumerate(headlines):
            table.add_row(str(index + 1), headline[0])

        self.console.print(table, justify="center")


    def display_article_summary(self,link: str):
        #TODO Change headlines to whatever response is
        # if headline in headlines:
        #     self.console.print(f'[u]{Panel(get_summary(link))}', justify="center")
        self.console.print(Panel(get_headlines()[0][1]), Panel(get_headlines()[0][1]), justify="center")
        self.console.print(f'Input (r)eturn to return to the main menu or type (q) to quit', justify="center")



# inspect('', methods=True)
# inspect(Panel, methods=True)
menu = Menu()
menu.display_article_summary('Hello')
# menu.ascii_art()
# # menu.progress_bar()
# menu.make_headlines_table()
# menu.categories_panel()
# menu.query_user()
# menu.get_user_input()
# menu.display_category_news('Business')