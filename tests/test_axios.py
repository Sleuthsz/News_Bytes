import pytest
from mockito import when, ANY, mock, unstub
from selenium.webdriver.remote.webelement import WebElement

from news_scraper.axios import Axios


@pytest.fixture
def setup():
    axios = Axios()
    return axios


def test_get_local_news(setup):
    item = WebElement(ANY, ANY)
    main_content = [item]
    a = mock({
        "text": "some headline"
    })
    when(setup.driver).execute(ANY(str), ANY(dict)).thenReturn(ANY(dict))
    when(setup.driver).find_elements(ANY(str), ANY(str)).thenReturn(main_content)
    when(item).find_element(ANY(str), ANY(str)).thenReturn(a)
    when(a).get_attribute(ANY(str)).thenReturn("www.some-url.com")

    headlines_and_links = setup.get_local_news("seattle")

    assert len(headlines_and_links) == 1
    assert headlines_and_links[0][0] == "some headline"
    assert headlines_and_links[0][1] == "www.some-url.com"
    unstub()


def test_get_article_text(setup):
    par1 = mock({
        "text": "some article text"
    })
    par2 = mock({
        "text": "some other article text"
    })
    when(setup.driver).execute(ANY(str), ANY(dict)).thenReturn(ANY(dict))
    when(setup.driver).find_elements(ANY(str), ANY(str)).thenReturn([par1, par2])

    article_text = setup.get_article_text("www.some-url.com")

    assert "some article text" in article_text
    unstub()
