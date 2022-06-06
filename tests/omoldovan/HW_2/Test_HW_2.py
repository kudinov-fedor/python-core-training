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
    time.sleep(5)
    yield session
    session.quit()
    time.sleep(2)

@pytest.mark.skip
def test_full_name(session):
    session.get(HOST + '/text-box')
    full_name = session.find_element(By.CSS_SELECTOR, '#userName')
    full_name.send_keys("Oleksandr")
    time.sleep(2)
    submit_btn = session.find_element(By.CSS_SELECTOR, '#submit')
    submit_btn.click()
    time.sleep(2)
    result = session.find_element(By.CSS_SELECTOR, '#output #name').text
    assert result == "Name:Oleksandr"


@pytest.mark.skip
def test_email(session):
    session.get(HOST + '/text-box')
    user_mail = session.find_element_by_css_selector('#userEmail')
    user_mail.send_keys('ababagalamaga@gmail.com')
    time.sleep(2)
    submit_btn = session.find_element(By.CSS_SELECTOR, '#submit')
    submit_btn.click()
    time.sleep(2)
    result = session.find_element(By.CSS_SELECTOR, '#output #email').text
    assert result == "Email:ababagalamaga@gmail.com"


# def test_incorrect_email(session):
#     session.get(HOST + '/text-box')
#     user_mail = session.find_element_by_css_selector('#userEmail')
#     user_mail.send_keys('ababagalamaga')
#     time.sleep(2)
#     submit_btn = session.find_element(By.CSS_SELECTOR, '#submit')
#     submit_btn.click()
#     time.sleep(2)
#     result = session.find_element(By.CSS_SELECTOR, '#userEmail')
#     class_name =                                                      # How to get the class name from web element
#     assert class_name == "mr-sm-2 field-error form-control"

def current_address(session):
    session.get(HOST + '/text-box')
    currentAddress = session.find_element_by_css_selector('#currentAddress')
    currentAddress.send_keys('Vasylkivska 49/34234 A')
    time.sleep(2)
    submit_btn = session.find_element(By.CSS_SELECTOR, '#submit')
    submit_btn.click()
    time.sleep(2)
    result = session.find_element(By.CSS_SELECTOR, '#output #currentAddress').text
    assert result == "Current Address :Vasylkivska 49/34234 A"


def permanenet_address(session):
    session.get(HOST + '/text-box')
    permanentAddress = session.find_element_by_css_selector('#permanentAddress')
    permanentAddress.send_keys('Vasylkivska 49/34234 A')
    time.sleep(2)
    submit_btn = session.find_element(By.CSS_SELECTOR, '#submit')
    submit_btn.click()
    time.sleep(2)
    result = session.find_element(By.CSS_SELECTOR, '#output #permanentAddress').text
    assert result == "Permananet Address :Vasylkivska 49/34234 B"

@pytest.mark.skip
def test_that_output_not_appears():   # All fields are empty
    session.get(HOST + '/text-box')
    time.sleep(2)
    submit_btn = session.find_element(By.CSS_SELECTOR, '#submit')
    submit_btn.click()
    result = session.find_element_by_css_selector('#output')
