from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Guardian:
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.theguardian.com")
    driver.implicitly_wait(1)

    def get_news_headlines(self):
        link = self.driver.find_elements(By.CLASS_NAME, "fc-item__link")

        headlines_links = []
        for i in range(10):
            headlines_links.append((link[i].text, link[i].get_attribute('href')))

        return headlines_links

    def get_business_headlines(self):
        self.driver.get('https://www.theguardian.com/us/business')
        link = self.driver.find_elements(By.CLASS_NAME, "fc-item__link")

        business_headlines_links = []
        for i in range(10):
            business_headlines_links.append((link[i].text, link[i].get_attribute('href')))

        return business_headlines_links

    def get_world_news_headlines(self):
        self.driver.get('https://www.theguardian.com/world')
        link = self.driver.find_elements(By.CLASS_NAME, "fc-item__link")

        world_headlines_links = []
        for i in range(10):
            world_headlines_links.append((link[i].text, link[i].get_attribute('href')))

        return world_headlines_links

    def get_tech_headlines(self):
        self.driver.get('https://www.theguardian.com/us/technology')
        link = self.driver.find_elements(By.CLASS_NAME, "fc-item__link")

        tech_headlines_links = []
        for i in range(10):
            tech_headlines_links.append((link[i].text, link[i].get_attribute('href')))

        return tech_headlines_links

    def get_sports_headlines(self):
        self.driver.get('https://www.theguardian.com/us/sport')
        link = self.driver.find_elements(By.CLASS_NAME, "fc-item__link")

        sports_headlines_links = []
        for i in range(10):
            sports_headlines_links.append((link[i].text, link[i].get_attribute('href')))

        return sports_headlines_links

    def get_article_text(self, link):
        self.driver.get(link)
        article = self.driver.find_element(By.TAG_NAME, "article")
        elements = article.find_elements(By.TAG_NAME, "p")

        text = ""
        for element in elements:
            text += element.text
        return text


if __name__ == "__main__":
    guardian = Guardian()
    news = guardian.get_news_headlines()
    business = guardian.get_business_headlines()
    world_news = guardian.get_world_news_headlines()
    tech = guardian.get_tech_headlines()
    sports = guardian.get_sports_headlines()
    # print(sports)
    print(guardian.get_article_text(sports[0][1]))
