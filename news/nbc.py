from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()
# nbc_key = os.getenv("NBC_KEY")
# GET https://newsapi.org/v2/top-headlines?country=us&apiKey=nbc_key

options = Options()
options.headless = True

homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")


nbc_driver = webdriver.Chrome(options=options, service=webdriver_service)

nbc_driver.get("https://www.nbcnews.com")
nbc_driver.implicitly_wait(1)


def get_headlines():
    link = nbc_driver.find_elements(By.CLASS_NAME, "related-content__headline-link")

    headlines_links = []
    for i in range(len(link)):
        headlines_links.append((link[i].text, link[i].get_attribute('href')))
        # print(link[i].get_attribute('href'))

    return headlines_links


def get_article_text(link):
    nbc_driver.get(link)
    article = nbc_driver.find_element(By.TAG_NAME, "article")
    elements = article.find_elements(By.XPATH, "//div[@data-component='text-block']")
    text = ""
    for element in elements:
        text += element.text
    return text


def get_business():
    # business_link = https://www.nbcnews.com/business
    pass


def get_world():
    # world_link = https://www.nbcnews.com/world
    pass


def get_tech():
    # tech_link = https://www.nbcnews.com/tech-media
    pass


def get_sports():
    # sports_link = https://www.nbcsports.com/?cid=eref:nbcnews:text
    pass


# too broad - refactor needed
# def get_categories():
#     categories_link = nbc_driver.find_elements(By.CLASS_NAME, "shortcuts-list-item")
#     category = nbc_driver.find_element(By.TAG_NAME, "li")
#     categories = []
#     for i in range(len(categories_link)):
#         categories.append((categories_link[i].text, categories_link[i].get_attribute('li')))
#         print(categories_link[i].get_attribute('li'))
#
#     return get_categories()

# ********* README.md update - created nbc.py for webscrape of nbc website, updated README.md - December 14, 2022
# ********* README.md update - finalized headline and link scrape, started categories scrape, updated README.md. -
# December 15, 2022

if __name__ == "__main__":
    headlines = get_headlines()
    print(headlines)
    links = get_article_text(headlines[1][1])
    print(links)
    # article_test = get_article_text()
    # print(article_test)
    # categories = get_categories()
    # print()

    # ------------------unused until able to get rest working-------------
    # article_text = get_article_text(links[1][1])
    # summary = get_summary(article_text)
    # print(summary)
    # print(article_text)
    # get_article_text()


# --------

# homedir = os.path.expanduser("~")
# webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")
#
# driver = webdriver.Chrome(options=options, service=webdriver_service)
# driver.get("https://www.nbcnews.com/")
# driver.implicitly_wait(1)

#
# def get_summary(text):
#     prompt = f"{text}\n\nTl;dr"
#     response = openai.Completion.create(
#         model=openai_model,
#         prompt=prompt,
#         temperature=0.7,
#         max_tokens=140,
#         top_p=1.0,
#         frequency_penalty=0.0,
#         presence_penalty=1
#     )
#     return response["choices"][0]["text"]
#
#
