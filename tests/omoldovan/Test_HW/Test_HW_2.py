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

@pytest.mark.skip
def test_full_name(session):
    session.get(HOST + '/text-box')
    full_name = session.find_element(By.CSS_SELECTOR, '#userName')
    full_name.send_keys("Oleksandr")
    submit_btn = session.find_element(By.CSS_SELECTOR, '#submit')
    submit_btn.click()
    result = session.find_element(By.CSS_SELECTOR, '#output #name').text
    assert result == "Name:Oleksandr"


@pytest.mark.skip
def test_email(session):
    session.get(HOST + '/text-box')
    user_mail = session.find_element_by_css_selector('#userEmail')
    user_mail.send_keys('ababagalamaga@gmail.com')
    submit_btn = session.find_element(By.CSS_SELECTOR, '#submit')
    submit_btn.click()
    result = session.find_element(By.CSS_SELECTOR, '#output #email').text
    assert result == "Email:ababagalamaga@gmail.com"


def test_incorrect_email(session):
    session.get(HOST + '/text-box')
    user_mail = session.find_element_by_css_selector('#userEmail')
    user_mail.send_keys('ababagalamaga')
    submit_btn = session.find_element(By.CSS_SELECTOR, '#submit')
    submit_btn.click()
    result = session.find_element(By.CSS_SELECTOR, '#userEmail')
    class_name = result.get_attribute("class")
    assert class_name == "mr-sm-2 field-error form-control"

# box = driver.find_element_by_css_selector("#resizableBoxWithRestriction") ------ LEAVE IT HERE FOR EXAMPLE
# different parameters of item
# print(box.tag_name)                           # div
# print(box.location)                           # {'x': 318, 'y': 237}
# print(box.size)                               # {'height': 200, 'width': 200}
# print(box.get_attribute("style"))             # "width: 200px; height: 200px;"
# print(box.get_property("style"))              # ['width', 'height']
# print(box.value_of_css_property("width"))     # "200px"
# print(box.value_of_css_property("height"))    # "200px"


@pytest.mark.skip
def test_current_address(session):
    session.get(HOST + '/text-box')
    currentAddress = session.find_element_by_css_selector('#currentAddress')
    currentAddress.send_keys('Vasylkivska 49/34234 A')
    submit_btn = session.find_element(By.CSS_SELECTOR, '#submit')
    submit_btn.click()
    result = session.find_element(By.CSS_SELECTOR, '#output #currentAddress').text
    assert result == "Current Address :Vasylkivska 49/34234 A"


@pytest.mark.skip
def test_permanent_address(session): # ER --- TEST MUST FAILED
    session.get(HOST + '/text-box')
    permanentAddress = session.find_element_by_css_selector('#permanentAddress')
    permanentAddress.send_keys('Vasylkivska 49/34234 A')
    submit_btn = session.find_element(By.CSS_SELECTOR, '#submit')
    submit_btn.click()
    result = session.find_element(By.CSS_SELECTOR, '#output #permanentAddress').text
    assert result == "Permananet Address :Vasylkivska 49/34234 B"


def test_submit_with_empty_fields(session):   # All fields are empty
    output_elem = ['#output #permanentAddress', '#output #currentAddress', '#output #email', '#output #name']
    session.get(HOST + '/text-box')
    submit_btn = session.find_element(By.CSS_SELECTOR, '#submit')
    submit_btn.click()
    result = session.find_element_by_css_selector('#output')
    for i in output_elem:
        if result != i:
            print("The data was not filled in the fields")
            result = True
        else:
            print("There is some data  in the fields")
            result = False
        assert result == True



