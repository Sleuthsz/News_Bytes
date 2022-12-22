import pytest
import os
import mock
from rich import box
from rich.panel import Panel
import pyfiglet
from rich.table import Table
from news_scraper.menu import Menu


def test_query_user():
    news_menu = Menu()
    with mock.patch('builtins.input', return_value='1'):
        news_menu.query_user()

        news_menu.console.print.assert_called_with(Panel('Enter a [red underline]category [light_steel_blue]if you wish to see more headlines,\n otherwise enter in a [red underline]headline number [light_steel_blue]in order to get a summary \n with a link to the article. If you wish to quit, enter [red underline](q)uit'), justify="center", style='Bold')


    with mock.patch('builtins.input', return_value='q'):
        news_menu.query_user()


        news_menu.assertEqual(news_menu.console.print.call_count, 1)

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
    news_menu.clear_screen()

    captured = capsys.readouterr()

    assert captured.out == ""


def test_ascii_art():
    news_menu = Menu()
    mock_print = mock.Mock()

    news_menu.console.print = mock_print

    news_menu.ascii_art()


    mock_print.assert_called_with(pyfiglet.figlet_format("WELCOME TO\n NEWS BYTES", font="slant", width=200),
                                  justify="center")


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
    assert table.row_styles == ["cyan", "magenta"]
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




