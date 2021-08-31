
import time

from selenium.webdriver.remote.webdriver import WebDriver, By
from selenium.webdriver import ActionChains as AC


def test_drag_and_drop(session: WebDriver):

    session.get("https://www.seleniumeasy.com/test/drag-and-drop-demo.html")

    items = session.find_elements(By.CSS_SELECTOR, "#todrag > span")
    dropzone = session.find_element(By.ID, "mydropzone")

    # todo does not work
    AC(session).drag_and_drop(items[3], dropzone).perform()
    AC(session).click_and_hold(items[1]).pause(1).move_to_element(dropzone).pause(1).release(dropzone).perform()

    time.sleep(5)
    items = session.find_elements(By.CSS_SELECTOR, "#todrag > span")
    assert len(items) == 3
