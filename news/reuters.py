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
driver.get("https://www.reuters.com/")
driver.implicitly_wait(1)


def get_headlines():
    heads = driver.find_elements(By.XPATH, "//a[@data-testid='Heading']")

    headlines_links = []
    for i in range(10):
        # Remove subheading for some links
        head_only = heads[i].text.split('\n')[0]

        # Create tuple (headline, link)
        headlines_links.append((head_only, heads[i].get_attribute('href')))

    return headlines_links


def get_article_text(link):
    driver.get(link)
    article = driver.find_element(By.TAG_NAME, "article")
    elements = article.find_elements(By.XPATH, "//p")
    text = ""
    for element in elements:
        text += element.text
    return text

if __name__ == "__main__":
    #print(get_article_text('https://www.reuters.com/markets/us/fed-set-slow-pace-rate-hikes-inflation-grinch-loses
# -steam-2022-12-14/'))
    #print(get_article_text('https://www.reuters.com/legal/crypto-exchange-ftx-fights-bahamas-demand-data-access-2022
# -12-14/'))
    print(get_headlines())
