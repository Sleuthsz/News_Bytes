import os

import openai
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

options = Options()
options.headless = True

homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

driver = webdriver.Chrome(options=options, service=webdriver_service)
driver.get("https://www.msnbc.com")
driver.implicitly_wait(1)


def get_msnbc_top_headlines_and_top_links():
    top_news_elements = driver.find_elements(By.CLASS_NAME, "smorgasbord-meta-content__headline")
    top_headlines_and_top_links = []
    for top_news_element in top_news_elements:
        top_news_anchor_element = top_news_element.find_element(By.TAG_NAME, "a")
        top_news_link = top_news_anchor_element.get_attribute("href")
        if "/watch/" not in top_news_link:
            top_headlines_and_top_links.append((top_news_anchor_element.text, top_news_link))
    return top_headlines_and_top_links


def get_msnbc_article_text(link):
    driver.get(link)
    text = ""
    if "/rachel-maddow-show/" in link:
        blog_element = driver.find_element(By.CLASS_NAME, "showblog-body__content")
        paragraph_elements = blog_element.find_elements(By.TAG_NAME, "p")
        for paragraph_element in paragraph_elements:
            text += paragraph_element.get_attribute("textContent")
    else:
        article_element = driver.find_element(By.CLASS_NAME, "article-body__content")
        paragraph_elements = article_element.find_elements(By.TAG_NAME, "p")
        for paragraph_element in paragraph_elements:
            if paragraph_element.get_attribute("class") == "":
                text += paragraph_element.get_attribute("textContent")
    return text


if __name__ == '__main__':
    headlines_and_links = get_msnbc_top_headlines_and_top_links()
    for item in headlines_and_links:
        print(item[0])
        # article_text = get_msnbc_article_text(item[1])
        # print(article_text)
        # print("=====================================================")
