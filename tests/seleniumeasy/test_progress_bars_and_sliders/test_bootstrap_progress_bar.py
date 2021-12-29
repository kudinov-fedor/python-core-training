from selenium.webdriver.remote.webdriver import WebDriver, By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


def test_download_progress(session: WebDriver):

    session.get("https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html")

    upload_btn = session.find_element(By.ID, "cricle-btn")
    percent_locator = (By.CSS_SELECTOR, "#circle .percenttext")
    percent = session.find_element(*percent_locator)

    # start upload, if value did not change during 5 seconds stop the test
    upload_btn.click()
    value, new_value = percent.text, None
    while value != new_value:
        try:
            WebDriverWait(session, 5).until(EC.text_to_be_present_in_element(percent_locator, "100%"))
            break
        except TimeoutException:
            value, new_value = new_value, percent.text
    else:
        raise AssertionError("Percentage is stack on " + new_value)
