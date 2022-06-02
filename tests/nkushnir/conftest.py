import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

SELENIUM_HOST = 'http://127.0.0.1'
SELENIUM_PORT = '4444'

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.set_capability('marionette', True)
    driver = webdriver.Remote(
        command_executor=f'{SELENIUM_HOST}:{SELENIUM_PORT}/wd/hub',
        options=options
    )
    driver.maximize_window()
    yield driver
    driver.quit()
