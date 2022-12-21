import pytest
from mockito import when, ANY, unstub, mock
from selenium.webdriver.remote.webelement import WebElement

from news_scraper.cbs import CBS


@pytest.fixture
def setup():
    cbs_scraper = CBS()
    return cbs_scraper


def test_get_news_headlines(setup):
    headlines_and_links = [
        ("Some Headline", "www.someurl.com"),
        ("Some Other Headline", "www.someotherurl.com")
    ]
    when(setup).get_headlines_and_links(ANY(str), ANY(str)).thenReturn(headlines_and_links)
    frontpage_headlines_and_links = setup.get_news_headlines()
    assert len(frontpage_headlines_and_links) == 2
    assert frontpage_headlines_and_links[0][0] == headlines_and_links[0][0]
    assert frontpage_headlines_and_links[0][1] == headlines_and_links[0][1]
    unstub()


def test_get_business_headlines(setup):
    headlines_and_links = [
        ("Some Business Headline", "www.somebusinessurl.com"),
        ("Some Other Business Headline", "www.someotherbusinessurl.com")
    ]
    when(setup).get_headlines_and_links(ANY(str), ANY(str)).thenReturn(headlines_and_links)
    business_headlines_and_links = setup.get_business_headlines()
    assert len(business_headlines_and_links) == 2
    assert business_headlines_and_links[0][0] == headlines_and_links[0][0]
    assert business_headlines_and_links[0][1] == headlines_and_links[0][1]
    unstub()


def test_get_world_news_headlines(setup):
    headlines_and_links = [
        ("Some World News Headline", "www.someworldnewsurl.com"),
        ("Some Other World News Headline", "www.someotherworldnewsurl.com")
    ]
    when(setup).get_headlines_and_links(ANY(str), ANY(str)).thenReturn(headlines_and_links)
    world_headlines_and_links = setup.get_world_news_headlines()
    assert len(world_headlines_and_links) == 2
    assert world_headlines_and_links[0][0] == headlines_and_links[0][0]
    assert world_headlines_and_links[0][1] == headlines_and_links[0][1]
    unstub()


def test_get_tech_news_headlines(setup):
    headlines_and_links = [
        ("Some Tech News Headline", "www.sometechnewsurl.com"),
        ("Some Other Tech News Headline", "www.someothertechnewsurl.com")
    ]
    when(setup).get_headlines_and_links(ANY(str), ANY(str)).thenReturn(headlines_and_links)
    tech_headlines_and_links = setup.get_tech_headlines()
    assert len(tech_headlines_and_links) == 2
    assert tech_headlines_and_links[0][0] == headlines_and_links[0][0]
    assert tech_headlines_and_links[0][1] == headlines_and_links[0][1]
    unstub()


def test_get_sports_headlines(setup):
    headlines_and_links = [
        ("Some Sports News Headline", "www.somesportsnewsurl.com"),
        ("Some Other Sports News Headline", "www.someothersportsnewsurl.com")
    ]
    when(setup).get_sports_headlines_and_links(ANY(str)).thenReturn(headlines_and_links)
    sports_headlines_and_links = setup.get_sports_headlines()
    assert len(sports_headlines_and_links) == 2
    assert sports_headlines_and_links[0][0] == headlines_and_links[0][0]
    assert sports_headlines_and_links[0][1] == headlines_and_links[0][1]
    unstub()


def test_get_news_article_text(setup):
    headlines_and_links = [
        ("Some Headline", "www.someurl.com"),
        ("Some Other Headline", "www.someotherurl.com")
    ]
    content_element = WebElement(ANY, ANY)
    paragraph_element1 = mock({
        "text": "some paragraph text"
    })
    paragraph_element2 = mock({
        "text": "some other paragraph text"
    })
    when(setup).get_headlines_and_links(ANY(str), ANY(str)).thenReturn(headlines_and_links)
    when(setup.driver).execute(ANY(str), ANY(dict)).thenReturn(ANY(dict))
    when(setup.driver).find_element(ANY(str), ANY(str)).thenReturn(content_element)
    when(content_element).find_elements(ANY(str), ANY(str)).thenReturn([paragraph_element1, paragraph_element2])
    frontpage_headlines_and_links = setup.get_news_headlines()
    frontpage_article_text = setup.get_article_text(frontpage_headlines_and_links[0][1])
    assert "some paragraph text" in frontpage_article_text
    unstub()


def test_get_business_article_text(setup):
    headlines_and_links = [
        ("Some Business Headline", "www.somebusinessurl.com"),
        ("Some Other Business Headline", "www.someotherbusinessurl.com")
    ]
    content_element = WebElement(ANY, ANY)
    paragraph_element1 = mock({
        "text": "some business paragraph text"
    })
    paragraph_element2 = mock({
        "text": "some other business paragraph text"
    })
    when(setup).get_headlines_and_links(ANY(str), ANY(str)).thenReturn(headlines_and_links)
    when(setup.driver).execute(ANY(str), ANY(dict)).thenReturn(ANY(dict))
    when(setup.driver).find_element(ANY(str), ANY(str)).thenReturn(content_element)
    when(content_element).find_elements(ANY(str), ANY(str)).thenReturn([paragraph_element1, paragraph_element2])
    business_headlines_and_links = setup.get_business_headlines()
    business_article_text = setup.get_article_text(business_headlines_and_links[0][1])
    assert "some business paragraph text" in business_article_text
    unstub()


def test_get_world_news_article_text(setup):
    headlines_and_links = [
        ("Some World News Headline", "www.someworldnewssurl.com"),
        ("Some Other World News Headline", "www.someotherworldnewsurl.com")
    ]
    content_element = WebElement(ANY, ANY)
    paragraph_element1 = mock({
        "text": "some world news paragraph text"
    })
    paragraph_element2 = mock({
        "text": "some other world news paragraph text"
    })
    when(setup).get_headlines_and_links(ANY(str), ANY(str)).thenReturn(headlines_and_links)
    when(setup.driver).execute(ANY(str), ANY(dict)).thenReturn(ANY(dict))
    when(setup.driver).find_element(ANY(str), ANY(str)).thenReturn(content_element)
    when(content_element).find_elements(ANY(str), ANY(str)).thenReturn([paragraph_element1, paragraph_element2])
    world_headlines_and_links = setup.get_world_news_headlines()
    world_article_text = setup.get_article_text(world_headlines_and_links[0][1])
    assert "some world news paragraph text" in world_article_text
    unstub()


def test_get_tech_news_article_text(setup):
    headlines_and_links = [
        ("Some Tech Headline", "www.sometechurl.com"),
        ("Some Other Tech Headline", "www.someothertechurl.com")
    ]
    content_element = WebElement(ANY, ANY)
    paragraph_element1 = mock({
        "text": "some tech news paragraph text"
    })
    paragraph_element2 = mock({
        "text": "some other tech news paragraph text"
    })
    when(setup).get_headlines_and_links(ANY(str), ANY(str)).thenReturn(headlines_and_links)
    when(setup.driver).execute(ANY(str), ANY(dict)).thenReturn(ANY(dict))
    when(setup.driver).find_element(ANY(str), ANY(str)).thenReturn(content_element)
    when(content_element).find_elements(ANY(str), ANY(str)).thenReturn([paragraph_element1, paragraph_element2])
    tech_headlines_and_links = setup.get_tech_headlines()
    tech_article_text = setup.get_article_text(tech_headlines_and_links[0][1])
    assert "some tech news paragraph text" in tech_article_text
    unstub()


def test_get_sports_article_text(setup):
    headlines_and_links = [
        ("Some Sports News Headline", "www.somesportsnewsurl.com"),
        ("Some Other Sports News Headline", "www.someothersportsnewsurl.com")
    ]
    content_element = WebElement(ANY, ANY)
    paragraph_element1 = mock({
        "text": "some sports news paragraph text"
    })
    paragraph_element2 = mock({
        "text": "some other sports news paragraph text"
    })
    when(setup).get_sports_headlines_and_links(ANY(str)).thenReturn(headlines_and_links)
    when(setup.driver).execute(ANY(str), ANY(dict)).thenReturn(ANY(dict))
    when(setup.driver).find_element(ANY(str), ANY(str)).thenReturn(content_element)
    when(content_element).find_elements(ANY(str), ANY(str)).thenReturn([paragraph_element1, paragraph_element2])
    sports_headlines_and_links = setup.get_sports_headlines()
    sports_article_text = setup.get_article_text(sports_headlines_and_links[0][1])
    assert "some sports news paragraph text" in sports_article_text
    unstub()
