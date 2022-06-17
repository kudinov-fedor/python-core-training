import os
import pytest
import time
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

driver_path = os.environ.get("DRIVER_PATH", "chromedriver")
HOST = 'https://demoqa.com'


@pytest.fixture
def session():
    session = Chrome(driver_path)
    yield session
    session.quit()


def test_registration_correct(session):
    session.get(HOST + '/register')
    first_name = session.find_element_by_css_selector('#firstname')
    first_name.send_keys('AAAAAA')
    res = first_name.get_attribute('value')
    assert res == 'AAAAAA'

    last_name = session.find_element_by_css_selector('#lastname')
    last_name.send_keys('AAAAAA')
    res = last_name.get_attribute('value')
    assert res == 'AAAAAA'

    user_name = session.find_element_by_css_selector('#userName')
    user_name.send_keys('AAAAAA')
    res = user_name.get_attribute('value')
    assert res == 'AAAAAA'

    password = session.find_element_by_css_selector('#password')
    password.send_keys('asdqweASDQWE123!@#')
    res = password.get_attribute('value')
    assert res == 'asdqweASDQWE123!@#'

    # captcha = session.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div/div/span/div[4]')
    # res = captcha.get_attribute("aria-checked")
    # assert res == "true"

    register_button = session.find_element_by_css_selector('#register')
    register_button.click()




