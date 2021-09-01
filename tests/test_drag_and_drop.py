import pytest
import time

from selenium.webdriver.remote.webdriver import WebDriver, By
from selenium.webdriver import ActionChains as AC


@pytest.mark.xfail
def test_drag_and_drop(session: WebDriver):

    session.get("https://www.seleniumeasy.com/test/drag-and-drop-demo.html")

    items = session.find_elements(By.CSS_SELECTOR, "#todrag > span")
    dropzone = session.find_element(By.ID, "mydropzone")

    AC(session).drag_and_drop(items[3], dropzone).perform()
    # AC(session).click_and_hold(items[1]).pause(1).move_to_element(dropzone).pause(1).release(dropzone).perform()
    # AC(session)\
    #     .click_and_hold(items[1])\
    #     .pause(1)\
    #     .move_to_element(dropzone)\
    #     .pause(1)\
    #     .release()\
    #     .perform()

    # Cannot call non W3C standard command while in W3C mode
    # from selenium.webdriver import TouchActions as TA
    # TA(session)\
    #     .tap_and_hold(items[1].location["x"], items[1].location["y"])\
    #     .move(dropzone.location["x"], dropzone.location["y"])\
    #     .release(dropzone.location["x"], dropzone.location["y"]).perform()

    items = session.find_elements(By.CSS_SELECTOR, "#todrag > span")
    assert len(items) == 3


def test_drag_and_drop_jquery(session: WebDriver):
    from helpers.utills import wait_element

    session.get("https://jqueryui.com/draggable")
    session.switch_to.frame(0)

    # item = session.find_element(By.CSS_SELECTOR, "#draggable")
    item = session.find_element(By.ID, "draggable")
    AC(session).drag_and_drop_by_offset(item, item.location["x"] + 50, item.location["y"]).perform()
    item = session.find_element(By.ID, "draggable")
    AC(session).drag_and_drop_by_offset(item, item.location["x"] + 50, item.location["y"]).perform()
    item = session.find_element(By.ID, "draggable")
    AC(session).drag_and_drop_by_offset(item, item.location["x"], item.location["y"] + 50).perform()
    item = session.find_element(By.ID, "draggable")
    AC(session).drag_and_drop_by_offset(item, item.location["x"], item.location["y"] + 50).perform()
    time.sleep(1)
