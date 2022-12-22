from selenium.webdriver.common.by import By

from news_scraper.news import News


class CBS(News):
    FRONT_PAGE_URL = "https://www.cbsnews.com/"
    BUSINESS_PAGE_URL = f"{FRONT_PAGE_URL}moneywatch"
    WORLD_PAGE_URL = f"{FRONT_PAGE_URL}world"
    TECHNOLOGY_PAGE_URL = f"{FRONT_PAGE_URL}technology"
    SPORTS_PAGE_URL = "https://www.cbssports.com/"

    FRONT_PAGE_ID = "component-latest-news"
    BUSINESS_PAGE_ID = "component-topic-moneywatch"
    WORLD_PAGE_ID = "component-topic-world"
    TECHNOLOGY_PAGE_ID = "component-topic-technology"

    def __init__(self):
        super().__init__()

    def get_news_headlines(self):
        return self.get_headlines_and_links(CBS.FRONT_PAGE_URL, CBS.FRONT_PAGE_ID)

    def get_business_headlines(self):
        return self.get_headlines_and_links(CBS.BUSINESS_PAGE_URL, CBS.BUSINESS_PAGE_ID)

    def get_world_news_headlines(self):
        return self.get_headlines_and_links(CBS.WORLD_PAGE_URL, CBS.WORLD_PAGE_ID)

    def get_tech_headlines(self):
        return self.get_headlines_and_links(CBS.TECHNOLOGY_PAGE_URL, CBS.TECHNOLOGY_PAGE_ID)

    def get_sports_headlines(self):
        return self.get_sports_headlines_and_links(CBS.SPORTS_PAGE_URL)

    def get_headlines_and_links(self, link, element_id):
        article_headlines_and_links = []
        self.driver.get(link)
        latest_news_element = self.driver.find_element(By.ID, element_id)
        article_elements = latest_news_element.find_elements(By.TAG_NAME, "article")
        for article_element in article_elements:
            if article_element.text != "":
                heading_element = article_element.find_element(By.TAG_NAME, "h4")
                anchor_element = article_element.find_element(By.TAG_NAME, "a")
                link = anchor_element.get_attribute("href")
                if "/video/" not in link:
                    article_headlines_and_links.append((heading_element.text, link))
        return article_headlines_and_links

    def get_article_text(self, link):
        if CBS.SPORTS_PAGE_URL in link:
            return self.get_sports_article_text(link)
        else:
            self.driver.get(link)
            content_element = self.driver.find_element(By.CLASS_NAME, "content__body")
            paragraph_elements = content_element.find_elements(By.TAG_NAME, "p")
            text = ""
            for paragraph_element in paragraph_elements:
                text += paragraph_element.text
            return text

    def get_sports_headlines_and_links(self, link):
        article_headlines_and_links = []
        self.driver.get(link)
        wrapper_element = self.driver.find_element(By.CLASS_NAME, "top-marquee-wrap")
        main_heading_elements = wrapper_element.find_elements(By.CLASS_NAME, "image-icon-title")
        for main_heading_element in main_heading_elements:
            link = main_heading_element \
                .find_element(By.XPATH, "..") \
                .find_element(By.XPATH, "..") \
                .find_element(By.XPATH, "..") \
                .get_attribute("href")
            if link is not None and "/news/" in link:
                article_headlines_and_links.append((main_heading_element.text, link))
        other_heading_elements = wrapper_element.find_elements(By.CLASS_NAME, "article-list-stack-item-title")
        for other_heading_element in other_heading_elements:
            link = other_heading_element.find_element(By.XPATH, "..").get_attribute("href")
            article_headlines_and_links.append((other_heading_element.text, link))
        return article_headlines_and_links

    def get_sports_article_text(self, link):
        self.driver.get(link)
        text = ""
        if "/live/" in link:
            content_element = self.driver.find_element(By.CLASS_NAME, "LiveBlogIntro")
            paragraph_elements = content_element.find_elements(By.TAG_NAME, "p")
            for paragraph_element in paragraph_elements:
                text += paragraph_element.text
            return text
        else:
            content_element = self.driver.find_element(By.CLASS_NAME, "Article-bodyContent")
            paragraph_elements = content_element.find_elements(By.TAG_NAME, "p")
            text = ""
            for paragraph_element in paragraph_elements:
                text += paragraph_element.text
            return text


if __name__ == '__main__':
    cbs_scraper = CBS()

    articles = cbs_scraper.get_sports_headlines()
    for article in articles:
        print(cbs_scraper.get_article_text(article[1]))
        print(">>>>>>>>>>>>>>>>")
        # print(article[1])
