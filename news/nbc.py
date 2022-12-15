from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()
nbc_key = os.getenv("NBC_KEY")
# GET https://newsapi.org/v2/top-headlines?country=us&apiKey=nbc_key

options = Options()
options.headless = True

homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")


nbc_driver = webdriver.Chrome(options=options, service=webdriver_service)

nbc_driver.get("https://www.nbcnews.com/")
nbc_driver.implicitly_wait(1)

print(nbc_driver)


def get_headlines():
    link = nbc_driver.find_elements(By.CLASS_NAME, "tease-card__headline")

    headlines_links = []
    for i in range(10):
        headlines_links.append((link[i].text, link[i].get_attribute('href')))

    return headlines_links


# TODO: get links to populate correctly
def get_article_text(link):
    nbc_driver.get(link)
    article = nbc_driver.find_element(By.TAG_NAME, "article")
    elements = article.find_elements(By.XPATH, "//div[@data-component='text-block']")
    text = ""
    for element in elements:
        text += element.text
    return text


if __name__ == "__main__":
    headlines = get_headlines()
    print(headlines)
    # links = get_article_text(links)
    # print(links)

    # ------------------unused until able to get rest working-------------
    # article_text = get_article_text(links[1][1])
    # summary = get_summary(article_text)
    # print(summary)
    # print(article_text)
    # get_article_text()

# ********* README.md update - created nbc.py for webscrape of nbc website, updated README.md - December 14, 2022


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

