from selenium.webdriver.remote.webdriver import WebDriver
from python_at_2021.tests.akaiafiuk.constants import HOST


class Page:
    url = ''

    def __init__(self, session: WebDriver):
        self.host = HOST
        self.session = session

    def open(self):
        self.session.get(self.host + self.url)
        return self
