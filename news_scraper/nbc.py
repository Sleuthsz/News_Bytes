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
    driver = webdriver.Chrome(options=options, service=webdriver_service)
    driver.get("https://www.nbcnews.com")
    driver.implicitly_wait(1)

    def get_news_headlines(self):
        link = self.driver.find_elements(By.CLASS_NAME, "related-content__headline-link")

        headlines_links = []
        for i in range(len(link)):
            headlines_links.append((link[i].text, link[i].get_attribute('href')))
        # print(link[i].get_attribute('href'))

        return headlines_links

    def get_article_text(self, link):
        self.driver.get(link)
        article = self.driver.find_element(By.TAG_NAME, "article")
        elements = article.find_elements(By.XPATH, "//div[@data-component='text-block']")
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
                headlines_links.append((head, link))
                continue
        return headlines_links[0:10]
    #
    # def get_business_headlines(self):
    #     return self.get_category_headlines("https://www.nbcnews.com/business")
    #
    # def get_world_news_headlines(self):
    #     return self.get_category_headlines("https://www.nbcnews.com/world")
    #
    # def get_tech_headlines(self):
    #     return self.get_category_headlines("https://www.nbcnews.com/tech-media")

    def get_business_headlines(self):
        self.driver.get("https://www.nbcnews.com/business")
        section = self.driver.find_elements(By.TAG_NAME, 'section')[2]
        business_links = section.find_elements(By.TAG_NAME, 'a')

        business_headlines_links = []
        for element in business_links:
            link = element.get_attribute('href')
            try:
                head = element.find_element(By.TAG_NAME, 'h2').text
            except:
                business_headlines_links.append((head, link))
                continue
        return business_headlines_links[0:10]

    def get_world_news_headlines(self):
        self.driver.get('https://www.nbcnews.com/world')
        world_news_link = self.driver.find_elements(By.CLASS_NAME, "related-content__headline-link")

        world_news_headlines_links = []
        for i in range(len(world_news_link)):
            world_news_headlines_links.append((world_news_link[i].text, world_news_link[i].get_attribute('href')))
        # print(link[i].get_attribute('href'))
        #     self.get_article_text()
        return world_news_headlines_links

    def get_tech_headlines(self):
        self.driver.get('https://www.nbcnews.com/tech-media')
        tech_news_link = self.driver.find_elements(By.CLASS_NAME, "wide-tease-item__headline")

        tech_news_headlines_links = []
        for i in range(len(tech_news_link)):
            tech_news_headlines_links.append((tech_news_link[i].text, tech_news_link[i].value_of_css_property('data-activity-map=lead-package-link-2')))
        # print(link[i].get_attribute('href'))
        #     self.get_article_text()
        return tech_news_headlines_links

    def get_sports_headlines(self):
        self.driver.get('https://www.nbcsports.com/')
        self.driver.implicitly_wait(1)

        lis = self.driver.find_elements(By.XPATH, '//aside/div/div[2]/div/div/ul/li')

        headlines_links = []
        for li in lis:
            a = li.find_element(By.TAG_NAME, 'a')
            headlines_links.append((a.text, a.get_attribute('href')))
        return headlines_links


# nbc_key = os.getenv("NBC_KEY")
# GET https://newsapi.org/v2/top-headlines?country=us&apiKey=nbc_key

# ********* README.md update - created nbc.py for webscrape of nbc website, updated README.md - December 14, 2022
# ********* README.md update - finalized headline and link scrape, started categories scrape, updated README.md. -
# December 15, 2022
# ********* README.md update - created NBC class and refactored to methods. Troubleshooting methods working properly,
# updated README.md. - December 17, 2022
# ********* README.md update - refactored NBC class and refactored to methods. Troubleshooting methods with team pivot
# of method names and organization, updated README.md. - December 18, 2022


if __name__ == "__main__":
    nbc = NBC()
    # working
    headlines = nbc.get_news_headlines()
    # print(headlines)
    business = nbc.get_business_headlines()
    # print(business)
    world = nbc.get_world_news_headlines()
    # print(world)
    sports = nbc.get_sports_headlines()
    # print(sports)

    # not working

    categories = nbc.get_category_headlines()
    print(categories)

    # almost working
    tech = nbc.get_tech_headlines()
    # print(tech)

    # ------------------unused until able to get rest working-------------
    # article_text = get_article_text(links[1][1])
    # summary = get_summary(article_text)
    # print(summary)
    # print(article_text)
    # get_article_text()

# -------- code for ChatGPT

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
