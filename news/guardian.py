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
    # article = driver.find_element(By.TAG_NAME, "article")
    # elements = article.find_elements(By.XPATH, "//p")
    article = driver.find_element(By.XPATH, "//div[@id='maincontent']")
    elements = article.find_elements(By.XPATH, "//div/p")

    text = ""
    for element in elements:
        text += element.text
    return text


if __name__ == "__main__":
    links = get_headlines()
    # articles = get_article_text(links[0][1])
    print(links)
