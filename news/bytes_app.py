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
driver.get("https://www.bbc.com")
driver.implicitly_wait(1)

openai_model = "text-ada-001"
# openai_model = "text-babbage-001"
# openai_model = "text-curie-001"
# openai_model = "text-davinci-003"


def get_headlines():
    link = driver.find_elements(By.CLASS_NAME, "media__link")

    headlines_links = []
    for i in range(10):
        headlines_links.append((link[i].text, link[i].get_attribute('href')))

    return headlines_links


def get_article_text(link):
    driver.get(link)
    article = driver.find_element(By.TAG_NAME, "article")
    elements = article.find_elements(By.XPATH, "//div[@data-component='text-block']")
    text = ""
    for element in elements:
        text += element.text
    return text


def get_summary(text):
    prompt = f"{text}\n\nTl;dr"
    response = openai.Completion.create(
        model=openai_model,
        prompt=prompt,
        temperature=0.7,
        max_tokens=140,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=1
    )
    return response["choices"][0]["text"]


if __name__ == "__main__":
    links = get_headlines()
    article_text = get_article_text(links[0][1])
    summary = get_summary(article_text)
    print(summary)
