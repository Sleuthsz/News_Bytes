from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
from news_scraper.news import News


class Axios(News):
    def __init__(self):
        super().__init__()


    local_cities = ['atlanta', 'austin', 'boston', 'charlotte', 'chicago', 'columbus', 'dallas', 'denver', 'des moines',
                    'detroit', 'houston', 'miami', 'nashville', 'nw arkansas', 'philadelphia', 'phoenix', 'raleigh',
                    'richmond', 'salt lake city', 'san francisco', 'seattle', 'tampa bay', 'twin cities', 'washington dc']

    def get_local_news(self, city):

        if city.lower() not in self.local_cities:
            return 'City not found'

        if ' ' in city:
            tokens = city.lower().split()
            city = '-'.join(tokens)

        url = 'https://www.axios.com/local/' + city.lower()

        self.driver.get(url)
        self.driver.implicitly_wait(0.5)

        main_content = self.driver.find_elements(By.XPATH, '//*[@id="main-content"]//h2')

        headlines_links = []
        for item in main_content:
            a = item.find_element(By.TAG_NAME, 'a')
            headlines_links.append((a.text, a.get_attribute('href')))

        return headlines_links

    def get_article_text(self, link):
        self.driver.get(link)
        self.driver.implicitly_wait(1)

        pars = self.driver.find_elements(By.XPATH, '//*[@id="main-content"]/div[3]/div[2]/div[2]/div[2]/p')

        article = ''
        for par in pars:
            article += par.text

        return article


