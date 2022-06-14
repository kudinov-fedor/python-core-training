import os
import pytest
import time
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver

driver_path = os.environ.get("DRIVER_PATH", "chromedriver")


@pytest.fixture
def session():
    session = Chrome(driver_path)
    yield session
    session.quit()


def test_sample_1(session: WebDriver):
    session.get("https://www.google.com.ua")


def test_sample_2(session: WebDriver):
    session.get("https://www.google.com.ua")
