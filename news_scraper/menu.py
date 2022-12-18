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

import bbc, guardian, cbs, reuters, news



class Menu:
    def __init__(self):
        self.console = Console()
        self.bbc = bbc.BBC()
        self.guardian = guardian.Guardian()
        self.cbs = cbs.CBS()
        self.reuters = reuters.Reuters()
        self.news = news.News()



    def get_headlines(self):
        new_list = []
        bbc_news = self.bbc.get_news_headlines()
        guardian_news = self.guardian.get_news_headlines()
        cbs_news = self.cbs.get_news_headlines()
        reuters_news = self.reuters.get_news_headlines()

        new_list += bbc_news[0:2] + guardian_news[0:2] + cbs_news[0:2] + reuters_news[0:2]
        return new_list

    def ascii_art(self):
        self.console.print(pyfiglet.figlet_format("WELCOME TO\n NEWS BYTES", font="slant", width=200), justify="center")

    @staticmethod
    def progress_bar(lst:list):
        for _ in track(lst, description="[green], fetching articles"):
            time.sleep(0.02)


    def make_headlines_table(self):
        headlines = self.get_headlines()
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
    # def get_user_input():
    #     while True:
    #         user_input = Prompt.ask("Select a category", choices=['Business', 'World News', 'Tech', 'Sports'])
    #         if user_input.lower() == 'q' or user_input.lower() == 'quit':
    #             if Confirm.ask("Are you sure you would like to quit?"):
    #                 sys.exit()
    #         for i in range(1, 11):
    #             if user_input.lower() == str(i):






    def display_category_news(self, category:str, headlines: list[str]):
        table = Table(show_lines=True, row_styles=["cyan", "magenta"], title_justify="center", box=box.HEAVY_EDGE, highlight=True)

        table.add_column("#", justify="center")
        table.add_column(f'{category} news_scraper', justify="center")

        for index, headline in enumerate(headlines):
            table.add_row(str(index + 1), headline[0])

        self.console.print(table, justify="center")


    def display_article_summary(self,link):

        if 'reuters' in link:
            article = self.reuters.get_article_text(link)
            self.console.print(f'[u]{Panel(self.news.get_summary(article))}', justify="center")
        elif 'bbc' in link:
            article = self.bbc.get_article_text(link)

            summary = self.news.get_summary(article)
            print(summary)

            # self.console.print(f'[b]{Panel(summary)}')
        elif 'cbs' in link:
            article = self.cbsnews.get_article_text(link)
            self.console.print(f'[c]{Panel(self.news.get_summary(article))}')
        elif 'guardian' in link:
            article = self.guardian.get_article_text(link)
            self.console.print(f'[c]{Panel(self.news.get_summary(article))}')

        self.console.print(Panel(link), justify="center")

        self.console.print(f'Input (r)eturn to return to the main menu or type (q) to quit', justify="center")

    def main(self):
        self.ascii_art()
        self.make_headlines_table()
        self.categories_panel()
        self.query_user()




# inspect('', methods=True)
# inspect(Panel, methods=True)
menu = Menu()
# menu.main()
menu.display_article_summary('https://www.bbc.com/news/world-europe-64013052')
# # bbc_news = bbc.BBC()
# menu.get_headlines()
# # menu.display_article_summary('Hello')
# # menu.ascii_art()
# # # menu.progress_bar()
# menu.make_headlines_table(menu.get_headlines())
# menu.categories_panel()
# menu.query_user()
# menu.get_user_input()
# menu.display_category_news('Business')