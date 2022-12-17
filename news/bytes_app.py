import os
import openai
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class News:
    def __init__(self):
        self.title = ""
        self.env = load_dotenv()
        self.api_key= os.getenv("OPENAI_API_KEY")
        self.options = Options()
        self.homedir = os.path.expanduser("~")
        self.webdriver_service = Service(f"{self.homedir}/chromedriver/stable/chromedriver")
        self.driver = webdriver.Chrome(options=self.options, service=self.webdriver_service)
        self.ai_model = {
            'ada': "text-ada-001",
            'babbage': "text-babbage-001",
            'curie': "text-curie-001",
            'davinci': "text-davinci-001",
        }

    @staticmethod
    def get_summary(text):
        prompt = f"{text}\n\nTl;dr"
        response = openai.Completion.create(
            model=self.ai_model['ada'],
            prompt=prompt,
            temperature=0.7,
            max_tokens=140,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=1
        )
        return response["choices"][0]["text"]


class BBC(News):
    def __init__(self):
        super().__init__()
        self.driver = driver.get("https://www.bbc.com")
        self.driver.implicitly_wait(1)

    def get_headlines(self):
        link = self.driver.find_elements(By.CLASS_NAME, "media__link")
        headlines_links = []
        for i in range(10):
            headlines_links.append((link[i].text, link[i].get_attribute('href')))
        return headlines_links

    def get_article_text(self, link):
        self.driver.get(link)
        article = self.driver.find_element(By.TAG_NAME, "article")
        elements = article.find_elements(By.XPATH, "//div[@data-component='text-block']")
        text = ""
        for element in elements:
            text += element.text
        return text


if __name__ == "__main__":
    bbc_news = BBC()
    print(bbc_news.get_headlines())
