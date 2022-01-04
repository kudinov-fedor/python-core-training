import pytest
from selenium import webdriver


@pytest.fixture(scope='module')
def driver_init():
    #options = webdriver.ChromeOptions()
    #options.add_argument("--disable-popup-blocking")
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()
