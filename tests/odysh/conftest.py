import os

import pytest
from selenium import webdriver

DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH")


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.maximize_window()
    yield driver
    driver.quit()
