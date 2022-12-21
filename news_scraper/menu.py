from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from functools import lru_cache
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
import bbc, guardian, cbs, reuters, news, axios


class Menu:
    def __init__(self):
        self.console = Console()
        self.bbc = bbc.BBC()
        self.guardian = guardian.Guardian()
        self.cbs = cbs.CBS()
        self.reuters = reuters.Reuters()
        self.axios = axios.Axios()
        self.news = news.News()
        self.news_sources = [self.bbc, self.guardian, self.cbs, self.reuters]


    @lru_cache(maxsize=None)
    def get_headlines(self, category):

        headlines = []
        if category == "news" or category == "world news":
            text = category
        else:
            text = f"{category} news"
        with self.console.status(f"Getting {text}...", spinner="shark"):
            with ThreadPoolExecutor() as executor:
                for source in self.news_sources:
                    if category == "news":
                        future = executor.submit(source.get_news_headlines)
                    elif category == "business":
                        future = executor.submit(source.get_business_headlines)
                    elif category == "world news":
                        future = executor.submit(source.get_world_news_headlines)
                    elif category == "tech":
                        future = executor.submit(source.get_tech_headlines)
                    elif category == "sports":
                        future = executor.submit(source.get_sports_headlines)
                    elif category == "local news":
                        continue
                    else:
                        raise ValueError(f'Invalid category: {category}, please enter a valid category')
                    headlines += future.result()[:2]
        return headlines


    def ascii_art(self):
        self.console.print(pyfiglet.figlet_format("WELCOME TO\n NEWS BYTES", font="slant", width=200), justify="center")

    @staticmethod
    def clear_screen():
        # Windows
        if os.name == 'nt':
            os.system('cls')
        # Unix/Linux/MacOS
        else:
            os.system('clear')


    def make_headlines_table(self, headlines):
        table = Table(show_lines=True, row_styles=["cyan", "magenta"], title_justify="center", box=box.HEAVY_EDGE, highlight=True)

        table.add_column("#", justify="center")
        table.add_column("[i]Headlines", justify="center", style="light_steel_blue", header_style="light_sky_blue1")

        for index, headline in enumerate(headlines):
            table.add_row(str(index + 1),headline[0])
        self.console.print(table, justify="center")

    def categories_panel(self):
        news_list:list[str] = ['[magenta]Business', '[blue]World News', '[magenta]Tech', '[blue]Sports',
                               '[magenta]Local News']
        categories = [Panel(category, expand=True, box=box.HEAVY_EDGE) for category in news_list]
        self.console.print(Columns(categories), justify="center")

    def query_user(self):
        self.console.print(Panel('Enter a [red]category [white]if you wish to see more headlines,\n otherwise enter in a headline number in order to get a summary \n with a link to the article. If you wish to quit, enter (q)uit'), justify="center", style='Bold')


    def display_article_summary(self, link):
        """
        Checks if the news string is in the link parameter, if it is then it runs the sub function on it.
        It then prints the link for the source article, and then prints out a menu
        """
        def fetch_and_display_summary(source):
            # Sub function which calls get_article_text, get_summary on the source parameter
            article = source.get_article_text(link)
            get_summary = self.news.get_summary(article)
            self.console.print(Panel(get_summary, expand=True, box=box.HEAVY_EDGE, title='Summary', highlight=True),
                               justify="center")

        if 'reuters' in link:
            fetch_and_display_summary(self.reuters)
        elif 'bbc' in link:
            fetch_and_display_summary(self.bbc)
        elif 'cbs' in link:
            fetch_and_display_summary(self.cbs)
        elif 'guardian' in link:
            fetch_and_display_summary(self.guardian)
        elif 'axios' in link:
            fetch_and_display_summary(self.axios)

        self.console.print(Panel(link), justify="center")

        self.console.print(f'Input (r)eturn to return to the main menu or type (q) to quit', justify="center")

    def display_category_news(self, category, headlines):
        table = Table(show_lines=True, row_styles=["cyan", "magenta"], title_justify="center", box=box.HEAVY_EDGE, highlight=True)

        table.add_column("#", justify="center")
        if category.lower() == 'world news':
            table.add_column('WORLD NEWS', justify="center")
        else:
            table.add_column(f'{category.upper()} NEWS', justify="center")

        for index, headline in enumerate(headlines):
            table.add_row(str(index + 1), headline[0])

        self.console.print(table, justify="center")

    def get_category_headlines(self, user_input, all_headlines):
        """
        Grabs headlines based on user input and uses all_headlines which is reassigned to a dictionary
        and calls the get_headlines method based on the user input
        """
        category_methods = {
            "business": self.get_headlines(user_input),
            "world news": self.get_headlines(user_input),
            "tech": self.get_headlines(user_input),
            "sports": self.get_headlines(user_input),
            "local news": self.get_headlines(user_input)
        }

        all_headlines[user_input] = category_methods[user_input]
        self.display_category_news(user_input, all_headlines[user_input])

    def run_category_menu(self, category, all_headlines):
        # Called in the run_app method
        while True:
            #called method at 210
            self.get_category_headlines(category, all_headlines)
            category_input = input('> ')
            if category_input.lower() == 'r' or category_input.lower() == 'return':
                break
            elif category_input.lower() == 'q' or category_input.lower() == 'quit':
                sys.exit()
            if category_input.isnumeric():
                #this iterates through the all_headlines dictionary lists at 250
                for index, headline in enumerate(all_headlines[category]):
                    if index + 1 == int(category_input):
                        #checks the index of the specified list in the dictionary and sends the link which is attached to the key to display_article_summary
                        all_headlines_dict_key = all_headlines[category][int(category_input) - 1][1]
                        self.display_article_summary(all_headlines_dict_key)

                category_menu_input = input('> ')
                if category_menu_input.lower() == 'r' or category_menu_input.lower() == 'return':
                    break
                elif category_menu_input.lower() == 'q' or category_menu_input.lower() == 'quit':
                    sys.exit()

        self.console.print(f'Input (r)eturn to return to the main menu or type (q) to quit', justify="center")

    def display_main_menu(self, headlines):
        #called in the run_app method
        self.clear_screen()
        self.make_headlines_table(headlines)
        self.categories_panel()
        self.query_user()

    def display_local_news(self, city):
        with self.console.status(f"Getting local news from {city}...", spinner="shark"):
            local_news = self.axios.get_local_news(city)

        table = Table(show_lines=True, row_styles=["cyan", "magenta"], title_justify="center", box=box.HEAVY_EDGE,
                      highlight=True)

        table.add_column("#", justify="center")
        table.add_column("[i]Local News", justify="center", style="light_steel_blue", header_style="light_sky_blue1")

        for index, headline in enumerate(local_news):
            table.add_row(str(index + 1), headline[0])
        self.console.print(table, justify="center")

        return local_news

    def run_local_news(self):
        while True:
            local_input = input('Enter city: ')
            local_heads = self.display_local_news(local_input)

            if local_input.lower() == 'r' or local_input.lower() == 'return':
                break
            if local_input.lower() == 'q' or local_input.lower() == 'quit':
                sys.exit()

            local_input2 = input('> ')
            if local_input2.lower() == 'r' or local_input2.lower() == 'return':
                break
            if local_input2.lower() == 'q' or local_input2.lower() == 'quit':
                sys.exit()

            if local_input2.isnumeric():
                self.clear_screen()
                for index, headline in enumerate(local_heads):
                    if index + 1 == int(local_input2):
                        self.display_article_summary(headline[1])

                local_input3 = input('>')

                if local_input3.lower() == 'r' or local_input3.lower() == 'return':
                    break
                if local_input3.lower() == 'q' or local_input3.lower() == 'quit':
                    sys.exit()

    def run_app(self):
        categories = ["business", "world news", "tech", "sports", "local news"]
        all_headlines = {
            "business": None,
            "world news": None,
            "tech": None,
            "sports": None,
        }
        while True:
            headlines = self.get_headlines("news")
            self.display_main_menu(headlines)
            user_input = input('> ')
            if user_input.lower() == 'q' or user_input.lower() == 'quit':
                if Confirm.ask("Are you sure you would like to quit?"):
                    sys.exit()
                else:
                    continue
            elif user_input.lower() == 'r' or user_input.lower() == 'return':
                continue
            elif user_input.isnumeric():
                self.clear_screen()
                for index , headline in enumerate(headlines):
                    if index + 1 == int(user_input):
                        self.display_article_summary(headline[1])
                headline_input = input('> ')
                if headline_input.lower() == 'r' or headline_input.lower() == 'return':
                    continue
                if headline_input.lower() == 'q' or headline_input.lower() == 'quit':
                    sys.exit()
                else:
                    self.console.print(Panel(f'[red]Sorry, that is not a valid input'), justify='center')
            elif user_input.lower() in categories:
                if user_input.lower() == 'local news':
                    self.run_local_news()
                else:
                    self.run_category_menu(user_input.lower(), all_headlines)
                    if user_input.lower() == 'r' or user_input.lower() == 'return':
                        break
                    elif user_input.lower() == 'q' or user_input.lower() == 'quit':
                        sys.exit()

            else:
                self.console.print(Panel(f'Sorry, that is not a valid input'),justify='center')


    def main(self):
        self.clear_screen()
        self.ascii_art()
        self.run_app()



# inspect('', methods=True)
# inspect(Panel, methods=True)
menu = Menu()
menu.main()
# menu.display_article_summary('https://www.bbc.com/news/world-europe-64013052')
# # bbc_news = bbc.BBC()
# # menu.display_article_summary('Hello')
# # menu.ascii_art()
# # # menu.progress_bar()
# menu.make_headlines_table()
# menu.categories_panel()
# menu.query_user()
# menu.get_user_input()
# menu.display_category_news('Business')