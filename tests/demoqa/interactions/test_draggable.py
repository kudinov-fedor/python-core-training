from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC


def test_dragabble_cursor_center(host: str, session: WebDriver):
    session.maximize_window()

    session.get(host + "/dragabble")
    session.find_element(By.ID, "draggableExample-tab-cursorStyle").click()

    cursorCenter = session.find_element(By.ID, "cursorCenter")

    start_location = cursorCenter.location
    AC(session).click_and_hold(cursorCenter).move_by_offset(1, 1).release().perform()
    end_location = cursorCenter.location

    # approximately at the same place
    print(end_location["x"] - start_location["x"], end_location["y"] - start_location["y"])
    assert end_location["x"] - start_location["x"] == -6
    assert end_location["y"] - start_location["y"] == -5


def test_dragabble_cursor_top_left(host: str, session: WebDriver):

    session.maximize_window()

    session.get(host + "/dragabble")
    session.find_element(By.ID, "draggableExample-tab-cursorStyle").click()

    cursorTopLeft = session.find_element(By.ID, "cursorTopLeft")

    start_location = cursorTopLeft.location
    AC(session).click_and_hold(cursorTopLeft).move_by_offset(1, 1).release().perform()
    end_location = cursorTopLeft.location

    # approximately half left, half bottom
    print(end_location["x"] - start_location["x"], end_location["y"] - start_location["y"])
    assert end_location["x"] - start_location["x"] == cursorTopLeft.size["width"] / 2 + 5
    assert end_location["y"] - start_location["y"] == cursorTopLeft.size["height"] / 2 + 6


def test_dragabble_cursor_bottom(host: str, session: WebDriver):

    session.maximize_window()

    session.get(host + "/dragabble")
    session.find_element(By.ID, "draggableExample-tab-cursorStyle").click()

    cursorBottom = session.find_element(By.ID, "cursorBottom")

    start_location = cursorBottom.location
    AC(session).click_and_hold(cursorBottom).move_by_offset(1, 1).release().perform()
    end_location = cursorBottom.location

    # approximately half up
    print(end_location["x"] - start_location["x"], end_location["y"] - start_location["y"])
    assert end_location["x"] - start_location["x"] == 1
    assert end_location["y"] - start_location["y"] == -cursorBottom.size["height"] / 2 + 1
