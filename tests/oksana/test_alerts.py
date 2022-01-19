from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
import pytest


WEBSITE = "https://demoqa.com/alerts"
TIME_WAIT = 5


@pytest.fixture(autouse=True)
def reset_alert(driver):
    yield
    try:
        driver.switch_to.alert.accept()
    except NoAlertPresentException:
        pass


def test_see_an_alert(driver):
    """
    Click on a button and check the alert.text; Click Ok.
    """
    driver.get(WEBSITE)
    driver.find_element(By.ID, "alertButton").click()
    alert = WebDriverWait(driver, TIME_WAIT).until(EC.alert_is_present())
    alert_text = alert.text
    alert.accept()
    assert alert_text == "You clicked a button"


def test_see_an_alert_confirm_box_appear(driver):
    """
    Click on a button and check the alert is accepted, and the alert box text is correct.
    """
    driver.get(WEBSITE)
    driver.find_element(By.ID, "confirmButton").click()
    alert = WebDriverWait(driver, TIME_WAIT).until(EC.alert_is_present())
    alert.accept()
    assert driver.find_element(By.ID, "confirmResult").text == "You selected Ok"


def test_see_an_alert_confirm_box_appear_and_canceled(driver):
    """
    Click on a button and check the alert is dismissed and the box text is correct.
    """
    driver.get(WEBSITE)
    driver.find_element(By.ID, "confirmButton").click()
    alert = WebDriverWait(driver, TIME_WAIT).until(EC.alert_is_present())
    alert.dismiss()
    assert driver.find_element(By.ID, "confirmResult").text == "You selected Cancel"


def test_see_an_alert_prompt(driver):
    """
    Click on a button and fill in Test, and check the box text is correct.
    """
    driver.get(WEBSITE)
    driver.find_element(By.ID, "promtButton").click()
    alert = WebDriverWait(driver, TIME_WAIT).until(EC.alert_is_present())
    alert.send_keys("Test")
    alert.accept()
    assert driver.find_element(By.ID, "promptResult").text == "You entered Test"
