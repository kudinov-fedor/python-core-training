from selenium.webdriver.remote.webdriver import WebDriver, By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.common.exceptions import TimeoutException


def test_progress_bar(host: str, session: WebDriver):

    session.get(host + "/progress-bar")

    startStopButton = session.find_element_by_css_selector("#startStopButton")
    progressBarLocator = By.ID, "progressBar"
    progressBar = session.find_element(*progressBarLocator)

    # start progress, if value did not change during 5 seconds stop the test
    startStopButton.click()
    value, new_value = progressBar.text, None
    while value != new_value:
        try:
            Wait(session, 5).until(EC.text_to_be_present_in_element(progressBarLocator, "100%"))
            break
        except TimeoutException:
            value, new_value = new_value, progressBar.text
    else:
        raise AssertionError("Percentage is stack on " + new_value)
