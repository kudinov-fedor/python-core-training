from selenium.webdriver.remote.webdriver import WebDriver, By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait


def test_visible_after(host: str, session: WebDriver):

    session.get(host + "/dynamic-properties")
    visibleAfterLocator = By.ID, "visibleAfter"
    Wait(session, 10).until(EC.visibility_of_element_located(visibleAfterLocator))

    visibleAfter = session.find_element(*visibleAfterLocator)
    visibleAfter.click()


def test_enable_after(host: str, session: WebDriver):

    session.get(host + "/dynamic-properties")
    enableAfterLocator = By.ID, "enableAfter"
    Wait(session, 10).until(EC.element_to_be_clickable(enableAfterLocator))

    enableAfter = session.find_element(*enableAfterLocator)
    enableAfter.click()


def test_clolor_change(host: str, session: WebDriver):

    session.get(host + "/dynamic-properties")
    colorChangeLocator = By.CSS_SELECTOR, "#colorChange.text-danger"
    Wait(session, 10).until(EC.presence_of_element_located(colorChangeLocator))

    colorChange = session.find_element(*colorChangeLocator)
    colorChange.click()
