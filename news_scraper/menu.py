from concurrent.futures import ThreadPoolExecutor

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
import os
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
        start_time = time.time()
        # bbc_news = self.bbc.get_news_headlines()
        # guardian_news = self.guardian.get_news_headlines()
        # cbs_news = self.cbs.get_news_headlines()
        # reuters_news = self.reuters.get_news_headlines()
        #
        # new_list += bbc_news[0:2] + guardian_news[0:2] + cbs_news[0:2] + reuters_news[0:2]
        with ThreadPoolExecutor(max_workers=4) as executor:
            for i in range(4):
                if i == 0:
                    future = executor.submit(self.bbc.get_news_headlines)
                    new_list += future.result()[:2]
                if i == 1:
                    future = executor.submit(self.guardian.get_news_headlines)
                    new_list += future.result()[:2]
                if i == 2:
                    future = executor.submit(self.cbs.get_news_headlines)
                    new_list += future.result()[:2]
                if i == 3:
                    future = executor.submit(self.reuters.get_news_headlines)
                    new_list += future.result()[:2]
        print(f"Time Elapsed: {time.time() - start_time}")
        return new_list

    def ascii_art(self):
        self.console.print(pyfiglet.figlet_format("WELCOME TO\n NEWS BYTES", font="slant", width=200), justify="center")

    @staticmethod
    def progress_bar(lst:list):
        for _ in track(lst, description="[green], fetching articles"):
            time.sleep(0.02)

    @staticmethod
    def clear_screen():
        # Windows
        if os.name == 'nt':
            os.system('cls')
        # Unix/Linux/MacOS
        else:
            os.system('clear')


    def make_headlines_table(self):
        headlines = self.get_headlines()
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
        headlines = self.get_headlines()
        while True:
            user_input = input('> ')
            if user_input.lower() == 'q' or user_input.lower() == 'quit':
                if Confirm.ask("Are you sure you would like to quit?"):
                    sys.exit()
                continue
            try:
                index = int(user_input)
                if 0 <= index < len(headlines):
                    self.display_article_summary(headlines[index][1])
                    break
                else:
                    print("Invalid input")
            except ValueError:
                print("Invalid input")




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
            summary = self.news.get_summary(article)
            get_summary = self.news.get_summary(summary)
            self.console.print(Panel(get_summary, expand=True, box=box.HEAVY_EDGE, title='Summary', highlight=True), justify="center")
        elif 'bbc' in link:
            article = self.bbc.get_article_text(link)

            summary = self.news.get_summary(article)
            get_summary = self.news.get_summary(summary)
            self.console.print(Panel(get_summary, box=box.HEAVY_EDGE, title='Summary', highlight=True, width=100), justify="center")

        elif 'cbs' in link:
            article = self.cbs.get_article_text(link)
            summary = self.news.get_summary(article)
            get_summary = self.news.get_summary(summary)
            self.console.print(Panel(get_summary, expand=True, box=box.HEAVY2GE, title='Summary'), justify="center")
        elif 'guardian' in link:
            article = self.guardian.get_article_text(link)
            summary = self.news.get_summary(article)
            get_summary = self.news.get_summary(summary)
            self.console.print(Panel(get_summary, expand=True, box=box.HEAVY_EDGE, title='Summary', highlight=True), justify="center")

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
# menu.display_article_summary('https://www.bbc.com/news/world-europe-64013052')
# # bbc_news = bbc.BBC()
# menu.get_headlines()
# # menu.display_article_summary('Hello')
# # menu.ascii_art()
# # # menu.progress_bar()
menu.make_headlines_table()
# menu.categories_panel()
# menu.query_user()
# menu.get_user_input()
# menu.display_category_news('Business')