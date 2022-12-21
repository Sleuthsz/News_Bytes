from selenium.webdriver.common.by import By

import news


class Guardian(news.News):
    def __init__(self):
        super().__init__()

    def get_news_headlines(self):
        return self.get_headlines_and_links("https://www.theguardian.com")

    def get_business_headlines(self):
        return self.get_headlines_and_links("https://www.theguardian.com/us/business")

    def get_world_news_headlines(self):
        return self.get_headlines_and_links("https://www.theguardian.com/world")

    def get_tech_headlines(self):
        return self.get_headlines_and_links("https://www.theguardian.com/us/technology")

    def get_sports_headlines(self):
        return self.get_headlines_and_links("https://www.theguardian.com/us/sport")

    def get_article_text(self, link):
        self.driver.get(link)
        article = self.driver.find_element(By.TAG_NAME, "article")
        elements = article.find_elements(By.TAG_NAME, "p")

        text = ""
        for element in elements:
            text += element.text
        return text

    def get_headlines_and_links(self, link):
        self.driver.get(link)
        link = self.driver.find_elements(By.CLASS_NAME, "fc-item__link")

        headlines_links = []
        for i in range(10):
            headlines_links.append((link[i].text, link[i].get_attribute('href')))

        return headlines_links


