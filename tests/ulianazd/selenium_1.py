import os
import time
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver

driver_path = os.environ.get("DRIVER_PATH", "chromedriver")


@pytest.fixture
def session():
    session = Chrome(driver_path)
    time.sleep(2)
    yield session
    session.quit()
    time.sleep(2)


def test_sample1(session: WebDriver):
    # session = Chrome("C:/Users/UZ/Downloads/chromedriver_win32/chromedriver.exe")
    session.get("https://demoqa.com/books")


def test_sample2(session: WebDriver):
    session.get("https://demoqa.com/books")
