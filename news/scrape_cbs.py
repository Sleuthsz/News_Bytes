import os

import openai
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

FRONT_PAGE_URL = "https://www.cbsnews.com/"
BUSINESS_PAGE_URL = f"{FRONT_PAGE_URL}moneywatch"
WORLD_PAGE_URL = f"{FRONT_PAGE_URL}world"
TECHNOLOGY_PAGE_URL = f"{FRONT_PAGE_URL}technology"
SPORTS_PAGE_URL = "https://www.cbssports.com/"

FRONT_PAGE_ID = "component-latest-news"
BUSINESS_PAGE_ID = "component-topic-moneywatch"
WORLD_PAGE_ID = "component-topic-world"
TECHNOLOGY_PAGE_ID = "component-topic-technology"


class CBSNewsScraper:
    def __init__(self, driver, options):
        self.driver = driver
        self.options = options

    def get_cbs_headlines_and_links(self, link, element_id):
        article_headlines_and_links = []
        self.driver.get(link)
        latest_news_element = self.driver.find_element(By.ID, element_id)
        article_elements = latest_news_element.find_elements(By.TAG_NAME, "article")
        for article_element in article_elements:
            if article_element.text != "":
                heading_element = article_element.find_element(By.TAG_NAME, "h4")
                anchor_element = article_element.find_element(By.TAG_NAME, "a")
                link = anchor_element.get_attribute("href")
                if "/video/" not in link:
                    article_headlines_and_links.append((heading_element.text, link))
        return article_headlines_and_links

    def get_cbs_article_text(self, link):
        self.driver.get(link)
        content_element = self.driver.find_element(By.CLASS_NAME, "content__body")
        paragraph_elements = content_element.find_elements(By.TAG_NAME, "p")
        text = ""
        for paragraph_element in paragraph_elements:
            text += paragraph_element.text
        return text

    def get_cbs_sports_headlines_and_links(self, link):
        article_headlines_and_links = []
        self.driver.get(link)
        wrapper_element = self.driver.find_element(By.CLASS_NAME, "top-marquee-wrap")
        main_heading_elements = wrapper_element.find_elements(By.CLASS_NAME, "image-icon-title")
        for main_heading_element in main_heading_elements:
            link = main_heading_element \
                .find_element(By.XPATH, "..") \
                .find_element(By.XPATH, "..") \
                .find_element(By.XPATH, "..") \
                .get_attribute("href")
            if "/news/" in link:
                article_headlines_and_links.append((main_heading_element.text, link))
        other_heading_elements = wrapper_element.find_elements(By.CLASS_NAME, "article-list-stack-item-title")
        for other_heading_element in other_heading_elements:
            link = other_heading_element.find_element(By.XPATH, "..").get_attribute("href")
            if "/news/" in link and "/nfl/news/" not in link:
                article_headlines_and_links.append((other_heading_element.text, link))
        return article_headlines_and_links

    def get_cbs_sports_article_text(self, link):
        self.driver.get(link)
        content_element = self.driver.find_element(By.CLASS_NAME, "Article-bodyContent")
        paragraph_elements = content_element.find_elements(By.TAG_NAME, "p")
        text = ""
        for paragraph_element in paragraph_elements:
            text += paragraph_element.text
        return text


if __name__ == '__main__':
    homedir = os.path.expanduser("~")
    webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

    options = Options()
    options.headless = True

    driver = webdriver.Chrome(options=options, service=webdriver_service)
    driver.implicitly_wait(1)

    cbs_scraper = CBSNewsScraper(driver, options)

    # articles = cbs_scraper.get_cbs_headlines_and_links(FRONT_PAGE_URL, FRONT_PAGE_ID)
    # articles = cbs_scraper.get_cbs_headlines_and_links(WORLD_PAGE_URL, WORLD_PAGE_ID)
    # for article in articles:
    #     print(article[0])
    #     print("=========")
    #     print(article[1])
    #     print(">>>>>>>>>")
    sports_articles = cbs_scraper.get_cbs_sports_headlines_and_links(SPORTS_PAGE_URL)
    print(len(sports_articles))
    # for article in sports_articles:
    #     print(article[0])
    #     print("=========")
    #     print(article[1])
    #     print(">>>>>>>>>")
    #     print(cbs_scraper.get_cbs_sports_article_text(article[1]))
    #     print("=========")

