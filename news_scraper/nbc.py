from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
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
            head = element.find_element(By.TAG_NAME, 'h2').text
            headlines_links.append((head, link))
        return headlines_links[0:10]

    def get_tech_headlines(self):
        tech_headlines = []
        self.driver.get("https://www.nbcnews.com/tech-media")
        self.driver.implicitly_wait(1)
        section = self.driver.find_elements(By.TAG_NAME,'section')[2]
        links = section.find_elements(By.TAG_NAME, 'a')
        css_links = self.driver.find_elements(By.CLASS_NAME, "wide-tease-item__headline")

        for element, link in zip(css_links, links):
            # Set a maximum number of iterations
            max_iterations = 25
            num_iterations = 0

            # Keep trying to find a suitable link until the maximum number of iterations is reached
            while link.get_attribute('href') == 'https://www.nbcnews.com/nbcblk' or link.get_attribute('href') == 'https://www.nbcnews.com/' and num_iterations < max_iterations:
                link = self.driver.find_element(By.TAG_NAME, 'a')

                num_iterations += 1

            # If a suitable link was found, append the tuple to the tech_headlines list
            if num_iterations < max_iterations:
                tech_headlines.append((element.text, link.get_attribute('href')))

        print(tech_headlines)

        return tech_headlines

    def get_business_headlines(self):
        return self.get_category_headlines("https://www.nbcnews.com/business")

    def get_world_news_headlines(self):
        self.driver.get('https://www.nbcnews.com/world')
        world_news_link = self.driver.find_elements(By.CLASS_NAME, "related-content__headline-link")

        world_news_headlines_links = []
        for i in range(len(world_news_link)):
            world_news_headlines_links.append((world_news_link[i].text, world_news_link[i].get_attribute('href')))
        return world_news_headlines_links

    def get_sports_headlines(self):
        self.driver.get('https://www.nbcsports.com/')
        self.driver.implicitly_wait(1)

        lis = self.driver.find_elements(By.XPATH, '//aside/div/div[2]/div/div/ul/li')

        headlines_links = []
        for li in lis:
            a = li.find_element(By.TAG_NAME, 'a')
            headlines_links.append((a.text, a.get_attribute('href')))
        return headlines_links


if __name__ == '__main__':
    nbc_news = NBC()

    nbc_news.get_tech_headlines()

    for headline in nbcsnews.get_tech_headlines():
        print(headline)
