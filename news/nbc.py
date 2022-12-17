from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os


class NBC:
    options = Options()
    options.headless = True

    load_dotenv()
    homedir = os.path.expanduser("~")
    webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")
    nbc_driver = webdriver.Chrome(options=options, service=webdriver_service)
    nbc_driver.get("https://www.nbcnews.com")
    nbc_driver.implicitly_wait(1)

    def get_news_headlines(self):
        link = self.nbc_driver.find_elements(By.CLASS_NAME, "related-content__headline-link")

        headlines_links = []
        for i in range(len(link)):
            headlines_links.append((link[i].text, link[i].get_attribute('href')))
        # print(link[i].get_attribute('href'))

        return headlines_links

    def get_article_text(self, link):
        self.nbc_driver.get(link)
        article = self.nbc_driver.find_element(By.TAG_NAME, "article")
        elements = article.find_elements(By.XPATH, "//div[@data-component='text-block']")
        text = ""
        for element in elements:
            text += element.text
        return text

    def get_business_headlines(self):
        section = self.nbc_driver.find_elements(By.TAG_NAME, 'section')[2]
        business_links = section.find_elements(By.TAG_NAME, 'a')

        business_headlines_links = []
        for element in business_links:

            link = element.get_attribute('href')
            try:
                head = element.find_element(By.TAG_NAME, 'h2').text
            except:
                continue

            business_headlines_links.append((head, link))

        return business_headlines_links[0:10]

    def get_world_news_headlines(self):
        self.nbc_driver.get('https://www.nbcnews.com/world')
        world_news_link = self.nbc_driver.find_elements(By.CLASS_NAME, "wide-tease-item__headline")

        world_news_headlines_links = []
        for i in range(10):
            world_news_headlines_links.append((world_news_link[i].text, world_news_link[i].get_attribute('href')))
        # print(link[i].get_attribute('href'))
        #     self.get_article_text()
        return world_news_headlines_links

    def get_tech_headlines(self):
        self.nbc_driver.get('https://www.nbcnews.com/tech-media')
        tech_news_link = self.nbc_driver.find_elements(By.CLASS_NAME, "wide-tease-item__headline")

        tech_news_headlines_links = []
        for i in range(10):
            tech_news_headlines_links.append((tech_news_link[i].text, tech_news_link[i].get_attribute('href')))
        # print(link[i].get_attribute('href'))
        #     self.get_article_text()
        return tech_news_headlines_links

    def get_sports_headlines(self):
        self.nbc_driver.get('https://www.nbcsports.com/?cid=eref:nbcnews:text')
        sports_link = self.nbc_driver.find_elements(By.CLASS_NAME, "more-headlines__list-item")

        sports_links = []
        for i in range(len(sports_links)):
            sports_links.append((sports_link[i].text, sports_link[i].get_attribute('href')))
        # print(link[i].get_attribute('href'))
        return sports_link


# nbc_key = os.getenv("NBC_KEY")
# GET https://newsapi.org/v2/top-headlines?country=us&apiKey=nbc_key

# ********* README.md update - created nbc.py for webscrape of nbc website, updated README.md - December 14, 2022
# ********* README.md update - finalized headline and link scrape, started categories scrape, updated README.md. -
# December 15, 2022


if __name__ == "__main__":
    nbc = NBC()
    headlines = nbc.get_news_headlines()
    print(headlines)
    links = nbc.get_article_text(headlines[1][1])
    print(links)
    business = nbc.get_business_headlines()
    print(business)
    # tech = nbc.get_tech_headlines()
    # print(tech)--broken
    # sports = nbc.get_sports_headlines()
    # print(sports)
    # article_test = get_article_text()
    # print(article_test)
    # categories = get_categories()
    # print()

    # ------------------unused until able to get rest working-------------
    # article_text = get_article_text(links[1][1])
    # summary = get_summary(article_text)
    # print(summary)
    # print(article_text)
    # get_article_text()

# --------

# homedir = os.path.expanduser("~")
# webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")
#
# driver = webdriver.Chrome(options=options, service=webdriver_service)
# driver.get("https://www.nbcnews.com/")
# driver.implicitly_wait(1)

#
# def get_summary(text):
#     prompt = f"{text}\n\nTl;dr"
#     response = openai.Completion.create(
#         model=openai_model,
#         prompt=prompt,
#         temperature=0.7,
#         max_tokens=140,
#         top_p=1.0,
#         frequency_penalty=0.0,
#         presence_penalty=1
#     )
#     return response["choices"][0]["text"]
#
#
