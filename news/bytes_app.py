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
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.options = Options()
        self.options.headless = True
        self.homedir = os.path.expanduser("~")
        self.webdriver_service = Service(f"{self.homedir}/chromedriver/stable/chromedriver")
        self.driver = webdriver.Chrome(options=self.options, service=self.webdriver_service)
        self.ai_model = {
            'ada': "text-ada-001",
            'babbage': "text-babbage-001",
            'curie': "text-curie-001",
            'davinci': "text-davinci-001",
        }

    def get_summary(self, text):
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
        self.driver.implicitly_wait(1)

    def get_news_headlines(self):
        self.driver.get("https://www.bbc.com")
        heads = self.driver.find_elements(By.CLASS_NAME, "media__link")
        headlines_links = []
        for i in range(10):
            headlines_links.append((heads[i].text, heads[i].get_attribute('href')))
        return headlines_links

    def get_news_category(self, link):
        self.driver.get(link)
        links = self.driver.find_elements(By.CLASS_NAME, 'gs-c-promo-heading')

        headlines_links = []
        for element in links:
            link = element.get_attribute('href')
            if link is not None:
                head = element.find_element(By.TAG_NAME, 'h3').text

            if head is not '' and link is not None:
                headlines_links.append((head, link))

        return headlines_links[0:10]

    def get_business_headlines(self):
        return self.get_news_category('https://www.bbc.com/news/business')

    def get_world_news_headlines(self):
        return self.get_news_category('https://www.bbc.com/news/world')

    def get_tech_headlines(self):
        return self.get_news_category('https://www.bbc.com/news/technology')

    def get_sports_headlines(self):
        self.driver.get('https://www.bbc.com/sport')
        links = self.driver.find_elements(By.CLASS_NAME, 'e1f5wbog0')

        headlines_links = []
        for element in links:
            link = element.get_attribute('href')
            if link is not None:
                head = element.find_element(By.TAG_NAME, 'p').text

            if head is not '' and link is not None:
                headlines_links.append((head, link))

        return headlines_links[0:10]

    def get_article_text(self, link):
        self.driver.get(link)
        article = self.driver.find_element(By.TAG_NAME, "article")
        elements = article.find_elements(By.XPATH, "//div[@data-component='text-block']")

        if len(elements) == 0:
            elements = self.driver.find_elements(By.XPATH, '//article/div[1]/p')

        text = ""
        for element in elements:
            text += element.text
        return text


if __name__ == "__main__":
    bbc = BBC()
    #print(bbc.get_tech_headlines())
    #print(bbc.get_sports_headlines())
    #print(bbc.get_article_text('https://www.bbc.com/news/business-64010202'))
    print(bbc.get_article_text('https://www.bbc.com/sport/football/63926145'))
