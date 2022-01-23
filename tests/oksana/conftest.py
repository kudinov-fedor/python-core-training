from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
import chromedriver_binary


@pytest.fixture(scope="session")
def driver():
    chromeOptions = Options()
    chromeOptions.add_argument('--headless')
    chromeOptions.add_argument("--disable-extensions")
    chromeOptions.add_argument("--ignore-certificate-errors")
    chromeOptions.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(options=chromeOptions)
    yield driver
    driver.quit()
