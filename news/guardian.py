from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)
driver.get("https://www.theguardian.com")
driver.implicitly_wait(1)


def get_headlines():
    link = driver.find_elements(By.CLASS_NAME, "fc-item__link")

    headlines_links = []
    for i in range(10):
        headlines_links.append((link[i].text, link[i].get_attribute('href')))

    return headlines_links


def get_article_text(link):
    driver.get(link)
    article = driver.find_element(By.CLASS_NAME, "dcr-1t62qer")
    elements = article.find_elements(By.TAG_NAME, "p")

    text = ""
    for element in elements:
        text += element.text
    return text


def get_business_headlines():
    driver.get('https://www.theguardian.com/us/business')
    link = driver.find_elements(By.CLASS_NAME, "fc-item__link")

    business_headlines_links = []
    for i in range(10):
        business_headlines_links.append((link[i].text, link[i].get_attribute('href')))

    return business_headlines_links


def get_world_headlines():
    driver.get('https://www.theguardian.com/world')
    link = driver.find_elements(By.CLASS_NAME, "fc-item__link")

    world_headlines_links = []
    for i in range(10):
        world_headlines_links.append((link[i].text, link[i].get_attribute('href')))

    return world_headlines_links


def get_tech_headlines():
    driver.get('https://www.theguardian.com/us/technology')
    link = driver.find_elements(By.CLASS_NAME, "fc-item__link")

    tech_headlines_links = []
    for i in range(10):
        tech_headlines_links.append((link[i].text, link[i].get_attribute('href')))

    return tech_headlines_links


def get_sports_headlines():
    driver.get('https://www.theguardian.com/us/sport')
    link = driver.find_elements(By.CLASS_NAME, "fc-item__link")

    sports_headlines_links = []
    for i in range(10):
        sports_headlines_links.append((link[i].text, link[i].get_attribute('href')))

    return sports_headlines_links


if __name__ == "__main__":
    links = get_headlines()
    articles = get_article_text(links[0][1])
    world_news = get_world_headlines()
    business_news = get_business_headlines()
    tech_news = get_tech_headlines()
    sports_news = get_sports_headlines()
    print(sports_news)
