import os
# import openai
# from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

options = Options()
options.headless = True

homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

driver = webdriver.Chrome(options=options, service=webdriver_service)


def get_news_headlines(link="https://www.reuters.com/"):
    driver.get(link)
    driver.implicitly_wait(1)

    heads = driver.find_elements(By.XPATH, "//a[@data-testid='Heading']")

    headlines_links = []
    for i in range(10):
        # Remove subheading for some links
        head_only = heads[i].text.split('\n')[0]

        # Create tuple (headline, link)
        headlines_links.append((head_only, heads[i].get_attribute('href')))

    return headlines_links


def get_business_headlines():
    return get_news_headlines('https://www.reuters.com/business/')


def get_world_news_headlines():
    return get_news_headlines('https://www.reuters.com/world/')


def get_tech_headlines():
    return get_news_headlines('https://www.reuters.com/technology/')


def get_sports_headlines():
    return get_news_headlines('https://reuters.com/lifestyle/sports/')


def get_article_text(link):
    driver.get(link)
    driver.implicitly_wait(1)

    article = driver.find_element(By.TAG_NAME, "article")
    elements = article.find_elements(By.XPATH, "//p")
    text = ""
    for element in elements:
        text += element.text
    return text

if __name__ == "__main__":
    print(get_article_text('https://www.reuters.com/markets/us/fed-set-slow-pace-rate-hikes-inflation-grinch-loses-steam-2022-12-14/'))
    #print(get_article_text('https://www.reuters.com/legal/crypto-exchange-ftx-fights-bahamas-demand-data-access-2022
# -12-14/'))
    #print(get_sports_headlines())
