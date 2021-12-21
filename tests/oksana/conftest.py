from selenium import webdriver
import pytest
# import chromedriver_binary


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
