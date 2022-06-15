import os
import time
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

driver_path = os.environ.get("DRIVER_PATH", "chromedriver")
HOST = "https://demoqa.com"


@pytest.fixture
def session():
    session = Chrome(driver_path)
    session.maximize_window()
    time.sleep(2)
    yield session
    session.quit()
    time.sleep(2)


def test_practice(session):
    session.get(HOST + "/text-box")
    session.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    field = session.find_element(By.CSS_SELECTOR, "textarea#permanentAddress")
    field.send_keys("Lviv")
    submit = session.find_element(By.CSS_SELECTOR, "button#submit")
    submit.click()

    result_field = session.find_element(By.CSS_SELECTOR, "p#permanentAddress")
    assert result_field.text == "Permananet Address :Lviv"
