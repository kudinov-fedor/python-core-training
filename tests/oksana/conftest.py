from selenium import webdriver
import pytest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import chromedriver_binary


@pytest.fixture(scope="session")
def driver():
    caps = DesiredCapabilities.CHROME.copy()
    caps['goog:loggingPrefs'] = {'browser': 'ALL'}
    chromeOptions = Options()
    chromeOptions.add_argument('--headless')
    chromeOptions.add_argument("--disable-extensions")
    chromeOptions.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(desired_capabilities=caps, options=chromeOptions)
    yield driver
    driver.quit()
