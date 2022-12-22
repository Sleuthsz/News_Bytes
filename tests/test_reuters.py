import pytest
from mockito import unstub, when, ANY, mock
from selenium.webdriver.remote.webelement import WebElement

from news_scraper.reuters import Reuters


@pytest.fixture
def setup():
    reuters = Reuters()
    return reuters


def test_get_news_headlines(setup):
    head1 = mock({
        "text": "some headline\n",
    })
    head2 = mock({
        "text": "some other headline\n",
    })
    head3 = mock({
        "text": "some other headline\n",
    })
    head4 = mock({
        "text": "some other headline\n",
    })
    head5 = mock({
        "text": "some other headline\n",
    })
    head6 = mock({
        "text": "some other headline\n",
    })
    head7 = mock({
        "text": "some other headline\n",
    })
    head8 = mock({
        "text": "some other headline\n",
    })
    head9 = mock({
        "text": "some other headline\n",
    })
    head10 = mock({
        "text": "some other headline\n",
    })
    when(setup.driver).execute(ANY(str), ANY(dict)).thenReturn(ANY(dict))
    when(setup.driver) \
        .find_elements(ANY(str), ANY(str)) \
        .thenReturn(
        [
            head1,
            head2,
            head3,
            head4,
            head5,
            head6,
            head7,
            head8,
            head9,
            head10
        ]
    )
    when(head1).get_attribute(ANY(str)).thenReturn("www.some-news.com")

    headlines_and_links = setup.get_news_headlines()

    assert len(headlines_and_links) == 10
    assert headlines_and_links[0][0] == "some headline"
    assert headlines_and_links[0][1] == "www.some-news.com"
    unstub()


def test_get_business_headlines(setup):
    headlines_and_links = [
        ("some headline", "www.some-news.com"),
        ("some other headline", "www.some-other-news.com")
    ]

    when(setup).get_news_headlines(ANY(str)).thenReturn(headlines_and_links)

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

    when(setup).get_news_headlines(ANY(str)).thenReturn(headlines_and_links)

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

    when(setup).get_news_headlines(ANY(str)).thenReturn(headlines_and_links)

    tech_news_headlines_and_links = setup.get_tech_headlines()

    assert len(tech_news_headlines_and_links) == 2
    assert tech_news_headlines_and_links[0][0] == "some headline"
    assert tech_news_headlines_and_links[0][1] == "www.some-news.com"
    unstub()


def test_get_sports_headlines(setup):
    headlines_and_links = [
        ("some headline", "www.some-news.com"),
        ("some other headline", "www.some-other-news.com")
    ]

    when(setup).get_news_headlines(ANY(str)).thenReturn(headlines_and_links)

    sports_headlines_and_links = setup.get_sports_headlines()

    assert len(sports_headlines_and_links) == 2
    assert sports_headlines_and_links[0][0] == "some headline"
    assert sports_headlines_and_links[0][1] == "www.some-news.com"
    unstub()


def test_get_article_text(setup):
    element1 = mock({
        "text": "some paragraph text",
    })
    element2 = mock({
        "text": "some other paragraph text",
    })
    article = WebElement(ANY, ANY)

    when(setup.driver).execute(ANY(str), ANY(dict)).thenReturn(ANY(dict))
    when(setup.driver).find_element(ANY(str), ANY(str)).thenReturn(article)
    when(article).find_elements(ANY(str), ANY(str)).thenReturn([element1, element2])

    article_text = setup.get_article_text("https://reuters.com/lifestyle/sports/")

    assert "some paragraph text" in article_text
    unstub()
