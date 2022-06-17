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


def test_correct_login(session):
    session.get(HOST + '/login')
    user_name = session.find_element_by_css_selector('#userName')
    user_name.send_keys("OleksandrMoldovan")
    user_password = session.find_element_by_css_selector('#password')
    user_password.send_keys("asdqweASDQWE123!@#")
    login_btn = session.find_element_by_css_selector("#login")
    login_btn.click()
    time.sleep(5)
    res = session.current_url
    assert res == 'https://demoqa.com/profile'


def test_login_with_incorrect_login(session):
    login_list = [' ', 'Olek']
    password_list = ['asdqweASDQWE123!@#', ' ', 'Ababagalamaga']
    session.get(HOST + '/login')
    for i in login_list:
        user_name = session.find_element_by_css_selector('#userName')
        user_name.send_keys(i)
        for j in password_list:
            user_password = session.find_element_by_css_selector('#password').send_keys(Keys.CONTROL + Keys.BACKSPACE)
            user_password = session.find_element_by_css_selector('#password')
            user_password.send_keys(j)
            login_btn = session.find_element_by_css_selector("#login")
            login_btn.click()
            time.sleep(5)
            res = session.find_element_by_xpath('//*[@id="name"]').get_attribute('innerHTML')
            assert res == "Invalid username or password!"







