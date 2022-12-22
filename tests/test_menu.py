import pytest
import os
from news_scraper.menu import Menu


def test_get_headlines():
    news_menu = Menu()
    # Test getting news headlines
    assert len(news_menu.get_headlines("news")) > 0

    # Test getting business headlines
    assert len(news_menu.get_headlines("business")) > 0

    # Test getting world news headlines
    assert len(news_menu.get_headlines("world news")) > 0

    # Test getting tech headlines
    assert len(news_menu.get_headlines("world news")) > 0

    # Test getting sports headlines
    assert len(news_menu.get_headlines("tech")) > 0

    # Test getting local news headlines
    assert len(news_menu.get_headlines("sports")) > 0

    # Test getting headlines with invalid category
    with pytest.raises(ValueError) as error:
        menu.get_headlines("invalid category")
    assert str(error.value) == 'Invalid category: invalid category, please enter a valid category'


def test_clear_screen(capsys):
    news_menu = Menu()
    # Test clearing screen
    news_menu.clear_screen()

    captured = capsys.readouterr()

    assert captured.out == ""