from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from news_scraper.news import News
import os


class NBC(News):
    def __init__(self):
        super().__init__()

        self.driver.get("https://www.nbcnews.com")
        self.driver.implicitly_wait(1)

    def get_news_headlines(self):
        link = self.driver.find_elements(By.CLASS_NAME, "related-content__headline-link")

        headlines_links = []
        for i in range(len(link)):
            headlines_links.append((link[i].text, link[i].get_attribute('href')))

        return headlines_links

    def get_article_text(self, link):
        self.driver.get(link)
        article = self.driver.find_element(By.TAG_NAME, "article")
        elements = article.find_elements(By.TAG_NAME, 'p')
        text = ""
        for element in elements:
            text += element.text
        return text

    def get_category_headlines(self, link):
        self.driver.get(link)
        self.driver.implicitly_wait(1)
        section = self.driver.find_elements(By.TAG_NAME, 'section')[2]
        links = section.find_elements(By.TAG_NAME, 'a')

        headlines_links = []
        for element in links:

            link = element.get_attribute('href')
            try:
                head = element.find_element(By.TAG_NAME, 'h2').text
            except:
                continue

            headlines_links.append((head, link))

        return headlines_links[0:10]

    def get_business_headlines(self):
        return self.get_category_headlines("https://www.nbcnews.com/business")

    def get_world_news_headlines(self):
        return self.get_category_headlines("https://www.nbcnews.com/world")

    def get_tech_headlines(self):
        return self.get_category_headlines("https://www.nbcnews.com/tech-media")

    def get_sports_headlines(self):
        self.driver.get('https://www.nbcsports.com/')
        self.driver.implicitly_wait(1)

        lis = self.driver.find_elements(By.XPATH, '//aside/div/div[2]/div/div/ul/li')

        headlines_links = []
        for li in lis:
            a = li.find_element(By.TAG_NAME, 'a')
            headlines_links.append((a.text, a.get_attribute('href')))
        return headlines_links

