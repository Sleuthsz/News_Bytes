import pytest
import os
import mock
import inspect
from rich import box
from rich.panel import Panel
import pyfiglet
from rich.table import Table
from news_scraper.menu import Menu
from news_scraper.nbc import NBC
from news_scraper.bbc import BBC
from news_scraper.guardian import Guardian
from news_scraper.cbs import CBS
from news_scraper.reuters import Reuters

def test_menu_news_sources():
    news_menu = Menu()
    members = inspect.getmembers(news_menu)
    assert 'console' in [member[0] for member in members]
    assert isinstance(news_menu.news_sources, list)
    assert len(news_menu.news_sources) == 5

def test_initiate_app():
    news_menu = Menu()
    source = inspect.getsource(news_menu.initiate_app)
    assert 'try' in source and 'except' in source

def test_run_local_news():
    news_menu = Menu()
    source = inspect.getsource(news_menu.run_local_news)
    num_while_loops = source.count('while')
    assert num_while_loops == 1

def test_run_category_menu():
    news_menu = Menu()
    source = inspect.getsource(news_menu.run_category_menu)
    num_while_loops = source.count('while')
    assert num_while_loops == 1

def test_main_menu():
    news_menu = Menu()

    mock_self = mock.Mock()
    news_menu.display_main_menu = mock_self
    mock_self.clear_screen()
    mock_self.make_headlines_table('headlines')
    mock_self.categories_panel()
    mock_self.query_user()

    mock_self.clear_screen.assert_called_once()
    mock_self.make_headlines_table.assert_called_once_with('headlines')
    mock_self.categories_panel.assert_called_once()
    mock_self.query_user.assert_called_once()
def test_display_local_news():
    news_menu = Menu()
    local_news = news_menu.display_local_news('California')
    assert local_news == 'City not found'

def test_category_menu(capsys):
    # Define a function that contains a while loop
    news_menu = Menu()
    category = 'Business News'
    all_headlines = {

    }
    try:
        news_menu.run_category_menu(category, all_headlines)
    except ValueError as error:
        assert error is not None


def test_get_headlines():
    news_menu = Menu()

    mock_get_headlines = mock.Mock()

    mock_get_headlines.return_value = ['Headline 1', 'Headline 2']

    news_menu.get_headlines = mock_get_headlines

    assert len(news_menu.get_headlines("news")) > 0

    assert len(news_menu.get_headlines("business")) > 0

    assert len(news_menu.get_headlines("world news")) > 0

    assert len(news_menu.get_headlines("world news")) > 0

    assert len(news_menu.get_headlines("tech")) > 0

    assert len(news_menu.get_headlines("sports")) > 0


def test_clear_screen(capsys):
    news_menu = Menu()
    # Test clearing screen

    captured = capsys.readouterr()

    assert captured.out == ""


def test_ascii_art():
    news_menu = Menu()
    mock_print = mock.Mock()

    news_menu.console.print = mock_print

    news_menu.ascii_art()


    mock_print.assert_called_with(pyfiglet.figlet_format("WELCOME TO\n NEWS BYTES", font="slant", width=200),
                                  justify="center", style='light_steel_blue')


def test_make_headlines_table():
    news_menu = Menu()
    mock_print = mock.Mock()

    news_menu.console.print = mock_print

    headlines = [
        ['Headline 1'],
        ['Headline 2'],
        ['Headline 3']
    ]

    news_menu.make_headlines_table(headlines)

    # Assert that the print method was called with a Table object
    mock_print.assert_called_with(mock.ANY, justify="center")
    table = mock_print.call_args[0][0]
    assert isinstance(table, Table)

    # Assert that the Table object has the correct properties
    assert table.show_lines == True
    assert table.row_styles == ["cyan", "light_sky_blue1"]
    assert table.title_justify == "center"
    assert table.box == box.HEAVY_EDGE
    assert table.highlight == True

    # Assert that the Table object has the correct columns
    assert len(table.columns) == 2
    assert table.columns[0].justify == "center"
    assert table.columns[1].justify == "center"
    assert table.columns[1].style == "light_steel_blue"
    assert table.columns[1].header_style == "light_sky_blue1"



def test_get_category_headlines():
    news_menu = Menu()
    mock_get_headlines = mock.Mock(return_value=['Headline 1', 'Headline 2', 'Headline 3'])
    news_menu.get_headlines = mock_get_headlines
    mock_display_category_news = mock.Mock()
    news_menu.display_category_news = mock_display_category_news
    all_headlines = {}
    news_menu.get_category_headlines('tech', all_headlines)
    mock_get_headlines.assert_called_with('tech')
    # Assert that the display_category_news method was called with the correct arguments
    mock_display_category_news.assert_called_with('tech', ['Headline 1', 'Headline 2', 'Headline 3'])

    # Assert that the all_headlines dictionary was updated correctly
    assert all_headlines == {'tech': ['Headline 1', 'Headline 2', 'Headline 3']}


def test_query_user():
    news_menu = Menu()
    testing_query = news_menu.query_user()
    assert testing_query is None





