import pytest
from mockito import ANY, when, mock, unstub
from selenium.webdriver.remote.webelement import WebElement

from news_scraper.nbc import NBC


@pytest.fixture
def setup():
    nbc = NBC()
    return nbc


def test_get_news_headlines(setup):
    link = mock({
        "text": "some headline"
    })
    links = [link]

    when(setup.driver).find_elements(ANY(str), ANY(str)).thenReturn(links)
    when(link).get_attribute(ANY(str)).thenReturn("www.some-url.com")

    headlines_and_links = setup.get_news_headlines()

    assert len(headlines_and_links) == 1
    assert headlines_and_links[0][0] == "some headline"
    assert headlines_and_links[0][1] == "www.some-url.com"
    unstub()


def test_get_article_text(setup):
    article = WebElement(ANY, ANY)
    element1 = mock({
        "text": "some article text"
    })
    element2 = mock({
        "text": "some other article text"
    })
    when(setup.driver).execute(ANY(str), ANY(dict)).thenReturn(ANY(dict))
    when(setup.driver).find_element(ANY(str), ANY(str)).thenReturn(article)
    when(article).find_elements(ANY(str), ANY(str)).thenReturn([element1, element2])

    article_text = setup.get_article_text("www.some-url.com")

    assert "some article text" in article_text
    unstub()


def test_get_tech_headlines(setup):
    headlines_and_links = [
        ("some headline", "www.some-news.com"),
        ("some other headline", "www.some-other-news.com")
    ]

    when(setup).get_category_headlines(ANY(str)).thenReturn(headlines_and_links)

    tech_headlines_and_links = setup.get_tech_headlines()
    assert len(tech_headlines_and_links) == 2
    assert tech_headlines_and_links[0][0] == "some headline"
    assert tech_headlines_and_links[0][1] == "www.some-news.com"
    unstub()


def test_get_business_headlines(setup):
    headlines_and_links = [
        ("some headline", "www.some-news.com"),
        ("some other headline", "www.some-other-news.com")
    ]

    when(setup).get_category_headlines(ANY(str)).thenReturn(headlines_and_links)

    business_headlines_and_links = setup.get_business_headlines()
    assert len(business_headlines_and_links) == 2
    assert business_headlines_and_links[0][0] == "some headline"
    assert business_headlines_and_links[0][1] == "www.some-news.com"
    unstub()


def test_get_sports_headlines(setup):
    li = WebElement(ANY, ANY)
    a = mock({
        "text": "some headline"
    })
    when(setup.driver).execute(ANY(str), ANY(dict)).thenReturn(ANY(dict))
    when(setup.driver).find_elements(ANY(str), ANY(str)).thenReturn([li])
    when(li).find_element(ANY(str), ANY(str)).thenReturn(a)
    when(a).get_attribute(ANY(str)).thenReturn("www.some-url.com")

    sports_headlines_and_links = setup.get_sports_headlines()

    assert len(sports_headlines_and_links) == 1
    assert sports_headlines_and_links[0][0] == "some headline"
    assert sports_headlines_and_links[0][1] == "www.some-url.com"
    unstub()
