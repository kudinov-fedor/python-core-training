import os
import time
import pytest

from selenium.webdriver import Chrome, Opera, Firefox
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver_path = os.environ.get("DRIVER_PATH", "chromedriver")
HOST = 'https://demoqa.com'


@pytest.fixture()
def session():
    session = Chrome(driver_path)
    time.sleep(2)
    yield session
    session.quit()
    time.sleep(2)


def test_full_name_element_presence(session):
    session.get(HOST + "/text-box")
    label = session.find_element(By.CSS_SELECTOR, "label#userName-label.form-label")
    assert label.is_displayed()
    assert label.text == 'Full Name'


def test_email_element_presence(session):
    session.get(HOST + "/text-box")
    label = session.find_element(By.CSS_SELECTOR, "label#userEmail-label.form-label")
    assert label.is_displayed()
    assert label.text == 'Email'


def test_current_address_element_presence(session):
    session.get(HOST + "/text-box")
    label = session.find_element(By.CSS_SELECTOR, "label#currentAddress-label.form-label")
    assert label.is_displayed()
    assert label.text == 'Current Address'


def test_permanent_address_element_presence(session):
    session.get(HOST + "/text-box")
    label = session.find_element(By.CSS_SELECTOR, "label#permanentAddress-label.form-label")
    assert label.is_displayed()
    assert label.text == 'Permanent Address'


def test_full_name_input_field(session):
    session.get(HOST + "/text-box")
    field = session.find_element(By.CSS_SELECTOR, "input#userName")
    field.send_keys("test")
    session.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    submit = session.find_element(By.CSS_SELECTOR, "button#submit")
    submit.click()
    result_field = session.find_element(By.XPATH, "//p[@id='name']")
    assert result_field.text == "Name:test"


def test_email_input_field(session):
    session.get(HOST + "/text-box")
    field = session.find_element(By.CSS_SELECTOR, "input#userEmail.mr-sm-2.form-control")
    field.send_keys("test@gmail.com")
    session.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    submit = session.find_element(By.CSS_SELECTOR, "button#submit")
    submit.click()
    result_field = session.find_element(By.XPATH, "//p[@id='email']")
    assert result_field.text == "Email:test@gmail.com"


def test_email_error_input_field(session):
    session.get(HOST + "/text-box")
    field = session.find_element(By.CSS_SELECTOR, "input#userEmail.mr-sm-2.form-control")
    field.send_keys("test1")
    session.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    submit = session.find_element(By.CSS_SELECTOR, "button#submit")
    submit.click()
    session.execute_script("window.scrollTo(0,-document.body.scrollHeight)")
    result_field = session.find_element(By.CSS_SELECTOR, "input#userEmail.mr-sm-2.field-error.form-control")
    assert result_field.is_displayed()


def test_all_submit_form(session):
    session.get(HOST + "/text-box")
    name = session.find_element(By.CSS_SELECTOR, "input#userName")
    email = session.find_element(By.CSS_SELECTOR, "input#userEmail.mr-sm-2.form-control")
    currentAddress = session.find_element(By.CSS_SELECTOR, "textarea#currentAddress.form-control")
    permanentAddress = session.find_element(By.CSS_SELECTOR, "textarea#permanentAddress.form-control")

    name.send_keys("Yuliia Londarenko")
    email.send_keys("test@gmail.com")
    currentAddress.send_keys("CurrentAddress")
    permanentAddress.send_keys("Permanent Address")

    session.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    submit = session.find_element(By.CSS_SELECTOR, "button#submit")
    submit.click()

    result_field = session.find_element(By.CSS_SELECTOR, "div.border.col-md-12.col-sm-12")
    assert result_field.is_enabled()
    assert result_field.text == 'Name:Yuliia Londarenko\n' 'Email:test@gmail.com\n' 'Current Address :CurrentAddress\n' 'Permananet Address :Permanent Address'
