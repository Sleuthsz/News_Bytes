import os

import openai
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import bbc


class News:
    def __init__(self):
        self.title = ""
        self.env = load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.options = Options()
        self.options.headless = True
        self.homedir = os.path.expanduser("~")
        self.webdriver_service = Service(f"{self.homedir}/chromedriver/stable/chromedriver")
        self.driver = webdriver.Chrome(options=self.options, service=self.webdriver_service)
        self.driver.implicitly_wait(1)
        self.ai_model = {
            'ada': "text-ada-001",
            'babbage': "text-babbage-001",
            'curie': "text-curie-001",
            'davinci': "text-davinci-003",
        }

    def get_summary(self, text):
        prompt = f"{text}\n\nTl;dr"
        openai.api_key = self.api_key
        response = openai.Completion.create(
            model=self.ai_model['davinci'],
            prompt=prompt,
            temperature=0.7,
            max_tokens=140,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=1
        )
        return response["choices"][0]["text"]



