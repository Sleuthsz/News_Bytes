from selenium.webdriver.common.by import By

import news


class Reuters(news.News):
    def __init__(self):
        super().__init__()

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


