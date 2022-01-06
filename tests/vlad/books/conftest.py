import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from .pages import LoginPage
from .constants import USER, PASSWORD

@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome(
        executable_path=ChromeDriverManager().install(),
    )
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def login(driver):
    login_page = LoginPage(driver)
    login_page.open().login(USER, PASSWORD)
    yield driver
