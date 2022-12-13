from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)
driver.get("https://www.bbc.com")
driver.implicitly_wait(1)


def get_headlines():
    link = driver.find_elements(By.CLASS_NAME, "media__link")

    headlines_links = []
    for i in range(10):
        headlines_links.append((link[i].text, link[i].get_attribute('href')))

    return headlines_links


if __name__ == "__main__":
    print(get_headlines())
