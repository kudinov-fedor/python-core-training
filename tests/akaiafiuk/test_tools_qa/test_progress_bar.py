import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.common.exceptions import TimeoutException
from python_at_2021.tests.akaiafiuk.constants import HOST


START_STOP_BUTTON = By.CSS_SELECTOR, '#startStopButton'
PROGRESS_BAR = By.CSS_SELECTOR, '.progress'


def test_progress_bar_simple_approach(session):
    """Simple and stupid. Wait for exact time for the progress to be 100%"""
    session.get(HOST + '/progress-bar')
    session.find_element(*START_STOP_BUTTON).click()
    Wait(session, 15).until(EC.text_to_be_present_in_element(PROGRESS_BAR, '100%'))


@pytest.mark.new
def test_progress_bar_better_approach(session):
    """Wait for certain amount of time will the value is changed till it reaches 100%"""
    session.get(HOST + '/progress-bar')
    session.find_element(*START_STOP_BUTTON).click()
    progress_bar = session.find_element(*PROGRESS_BAR)
    value, new_value = progress_bar.text, None
    while value != new_value:
        try:
            Wait(session, 6).until(EC.text_to_be_present_in_element(PROGRESS_BAR, "100%"))
            break
        except TimeoutException:
            value, new_value = new_value, progress_bar.text
    else:
        raise AssertionError("Percentage is stuck on " + new_value)
