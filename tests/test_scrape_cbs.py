import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from news.scrape_cbs import CBSNewsScraper


@pytest.fixture
def setup():
    homedir = os.path.expanduser("~")
    webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

    options = Options()
    options.headless = True

    driver = webdriver.Chrome(options=options, service=webdriver_service)
    driver.implicitly_wait(1)

    cbs_scraper = CBSNewsScraper(driver, options)
    return cbs_scraper


def test_get_news_headlines(setup):
    frontpage_headlines_and_links = setup.get_news_headlines()
    assert len(frontpage_headlines_and_links) > 0


def test_get_business_headlines(setup):
    business_headlines_and_links = setup.get_business_headlines()
    assert len(business_headlines_and_links) > 0


def test_get_world_news_headlines(setup):
    world_headlines_and_links = setup.get_world_news_headlines()
    assert len(world_headlines_and_links) > 0


def test_get_tech_news_headlines(setup):
    tech_headlines_and_links = setup.get_tech_news_headlines()
    assert len(tech_headlines_and_links) > 0


def test_get_sports_headlines(setup):
    sports_headlines_and_links = setup.get_sports_headlines()
    assert len(sports_headlines_and_links) > 0


def test_get_news_article_text(setup):
    frontpage_headlines_and_links = setup.get_news_headlines()
    frontpage_article_text = setup.get_article_text(frontpage_headlines_and_links[0][1])
    assert len(frontpage_article_text) > 0


def test_get_business_article_text(setup):
    business_headlines_and_links = setup.get_business_headlines()
    business_article_text = setup.get_article_text(business_headlines_and_links[0][1])
    assert len(business_article_text) > 0


def test_get_world_news_article_text(setup):
    world_headlines_and_links = setup.get_world_news_headlines()
    world_article_text = setup.get_article_text(world_headlines_and_links[0][1])
    assert len(world_article_text) > 0


def test_get_tech_news_article_text(setup):
    tech_headlines_and_links = setup.get_tech_news_headlines()
    tech_article_text = setup.get_article_text(tech_headlines_and_links[0][1])
    assert len(tech_article_text) > 0


def test_get_sports_article_text(setup):
    sports_headlines_and_links = setup.get_sports_headlines()
    sports_article_text = setup.get_article_text(sports_headlines_and_links[0][1])
    assert len(sports_article_text) > 0
