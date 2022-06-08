import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(2)
    yield browser
    browser.quit()
