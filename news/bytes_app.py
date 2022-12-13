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


def get_headlines():
    link = driver.find_elements(By.CLASS_NAME, "media__link")

    headlines_links = []
    for i in range(10):
        headlines_links.append((link[i].text, link[i].get_attribute('href')))

    return headlines_links


if __name__ == "__main__":
    # print(get_headlines()
    links = get_headlines()
    print(links[1][1])
    print("==================")
    driver.get(links[1][1])
    element = driver.find_element(By.TAG_NAME, "article")
    print(element.text)
    prompt = f"Summarize this: {element.text}"
    # print(prompt)
    # response = openai.Completion.create(
    #     model="text-ada-001",
    #     prompt=prompt,
    #     temperature=0.6,
    # )
    # print("==================")
    #
    # print(response)
