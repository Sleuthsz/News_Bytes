import pytest
from mockito import ANY, when, unstub, mock
from selenium.webdriver.remote.webelement import WebElement

from news_scraper.guardian import Guardian


@pytest.fixture
def setup():
    guardian = Guardian()
    return guardian


def test_get_news_headlines(setup):
    headlines_and_links = [
        ("some headline", "www.some-news.com"),
        ("some other headline", "www.some-other-news.com")
    ]

    when(setup).get_headlines_and_links(ANY(str)).thenReturn(headlines_and_links)

    top_headlines_and_links = setup.get_news_headlines()
    assert len(top_headlines_and_links) == 2
    assert top_headlines_and_links[0][0] == "some headline"
    assert top_headlines_and_links[0][1] == "www.some-news.com"
    unstub()


def test_get_business_headlines(setup):
    headlines_and_links = [
        ("some headline", "www.some-news.com"),
        ("some other headline", "www.some-other-news.com")
    ]

    when(setup).get_headlines_and_links(ANY(str)).thenReturn(headlines_and_links)

    business_headlines_and_links = setup.get_business_headlines()
    assert len(business_headlines_and_links) == 2
    assert business_headlines_and_links[0][0] == "some headline"
    assert business_headlines_and_links[0][1] == "www.some-news.com"
    unstub()


def test_get_world_news_headlines(setup):
    headlines_and_links = [
        ("some headline", "www.some-news.com"),
        ("some other headline", "www.some-other-news.com")
    ]

    when(setup).get_headlines_and_links(ANY(str)).thenReturn(headlines_and_links)

    world_news_headlines_and_links = setup.get_world_news_headlines()
    assert len(world_news_headlines_and_links) == 2
    assert world_news_headlines_and_links[0][0] == "some headline"
    assert world_news_headlines_and_links[0][1] == "www.some-news.com"
    unstub()


def test_get_tech_headlines(setup):
    headlines_and_links = [
        ("some headline", "www.some-news.com"),
        ("some other headline", "www.some-other-news.com")
    ]

    when(setup).get_headlines_and_links(ANY(str)).thenReturn(headlines_and_links)

    tech_headlines_and_links = setup.get_tech_headlines()
    assert len(tech_headlines_and_links) == 2
    assert tech_headlines_and_links[0][0] == "some headline"
    assert tech_headlines_and_links[0][1] == "www.some-news.com"
    unstub()


def test_get_sports_headlines(setup):
    headlines_and_links = [
        ("some headline", "www.some-news.com"),
        ("some other headline", "www.some-other-news.com")
    ]

    when(setup).get_headlines_and_links(ANY(str)).thenReturn(headlines_and_links)

    sports_headlines_and_links = setup.get_sports_headlines()
    assert len(sports_headlines_and_links) == 2
    assert sports_headlines_and_links[0][0] == "some headline"
    assert sports_headlines_and_links[0][1] == "www.some-news.com"
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

    article_text = setup.get_article_text("www.some-news.com")

    assert "some article text" in article_text
    unstub()


def test_get_headlines_and_links(setup):
    link1 = mock({
        "text": "some headline"
    })
    link2 = mock({
        "text": "some other headline"
    })
    link3 = mock({
        "text": "some other headline"
    })
    link4 = mock({
        "text": "some other headline"
    })
    link5 = mock({
        "text": "some other headline"
    })
    link6 = mock({
        "text": "some other headline"
    })
    link7 = mock({
        "text": "some other headline"
    })
    link8 = mock({
        "text": "some other headline"
    })
    link9 = mock({
        "text": "some other headline"
    })
    link10 = mock({
        "text": "some other headline"
    })
    when(setup.driver).execute(ANY(str), ANY(dict)).thenReturn(ANY(dict))
    when(setup.driver)\
        .find_elements(ANY(str), ANY(str))\
        .thenReturn(
        [
            link1,
            link2,
            link3,
            link4,
            link5,
            link6,
            link7,
            link8,
            link9,
            link10
        ]
    )
    when(link1).get_attribute(ANY(str)).thenReturn("www.some-link.com")

    headlines_and_links = setup.get_headlines_and_links("www.some-news.com")

    assert len(headlines_and_links) == 10
    assert headlines_and_links[0][0] == "some headline"
    assert headlines_and_links[0][1] == "www.some-link.com"
    unstub()