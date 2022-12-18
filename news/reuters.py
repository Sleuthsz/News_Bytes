import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Reuters:
    options = Options()
    options.headless = True

    homedir = os.path.expanduser("~")
    webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

    driver = webdriver.Chrome(options=options, service=webdriver_service)

    def get_news_headlines(self, link="https://www.reuters.com/"):
        self.driver.get(link)
        self.driver.implicitly_wait(1)

        heads = self.driver.find_elements(By.XPATH, "//a[@data-testid='Heading']")

        headlines_links = []
        for i in range(10):
            # Remove subheading for some links
            head_only = heads[i].text.split('\n')[0]

            # Create tuple (headline, link)
            headlines_links.append((head_only, heads[i].get_attribute('href')))

        return headlines_links

    def get_business_headlines(self):
        return self.get_news_headlines('https://www.reuters.com/business/')

    def get_world_news_headlines(self):
        return self.get_news_headlines('https://www.reuters.com/world/')

    def get_tech_headlines(self):
        return self.get_news_headlines('https://www.reuters.com/technology/')

    def get_sports_headlines(self):
        return self.get_news_headlines('https://reuters.com/lifestyle/sports/')

    def get_article_text(self, link):
        self.driver.get(link)
        self.driver.implicitly_wait(1)

        article = self.driver.find_element(By.TAG_NAME, "article")
        elements = article.find_elements(By.XPATH, "//p")
        text = ""
        for element in elements:
            text += element.text
        return text


if __name__ == "__main__":
    reuters = Reuters()
    print(reuters.get_news_headlines())
    tech_headlines = reuters.get_tech_headlines()
    print(reuters.get_article_text(tech_headlines[0][1]))