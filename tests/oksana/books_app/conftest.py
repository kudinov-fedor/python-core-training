from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import pytest
from selenium.webdriver.chrome.options import Options
import chromedriver_binary


@pytest.fixture(scope="session")
def session() -> WebDriver:
    chromeOptions = Options()
    chromeOptions.add_argument('--headless')
    chromeOptions.add_argument("--disable-extensions")
    chromeOptions.add_argument("--ignore-certificate-errors")
    chromeOptions.add_argument("window-size=1920,1080")
    session = webdriver.Chrome(options=chromeOptions)
    yield session
    session.quit()
