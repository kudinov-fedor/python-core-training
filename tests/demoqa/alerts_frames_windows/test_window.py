import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait

import time


@pytest.fixture(autouse=True)
def close_child_windows(session):
    time.sleep(3)
    parent_window = session.current_window_handle
    yield
    windows = session.window_handles
    for w in windows:
        if w != parent_window:
            session.switch_to.window(w)
            session.close()
    session.switch_to.window(parent_window)


def test_new_tab(host: str, session: WebDriver):
    session.get(host + "/browser-windows")
    tabButton = session.find_element_by_css_selector("#tabButton")
    tabButton.click()

    Wait(session, 5).until(EC.number_of_windows_to_be(2))
    session.switch_to.window(session.window_handles[1])

    body = session.find_element_by_css_selector("body")
    assert body.text == "This is a sample page"


def test_new_window(host: str, session: WebDriver):

    session.get(host + "/browser-windows")
    windowButton = session.find_element_by_css_selector("#windowButton")
    windowButton.click()

    Wait(session, 5).until(EC.number_of_windows_to_be(2))
    session.switch_to.window(session.window_handles[1])

    body = session.find_element_by_css_selector("body")
    assert body.text == "This is a sample page"


@pytest.mark.skip("address to new window session stacks")
def test_new_message_window(host: str, session: WebDriver):

    session.get(host + "/browser-windows")
    messageWindowButton = session.find_element_by_css_selector("#messageWindowButton")
    messageWindowButton.click()

    Wait(session, 5).until(EC.number_of_windows_to_be(2))
    session.switch_to.window(session.window_handles[1])

    body = session.find_element_by_css_selector("body")
    assert body.text == "Knowledge increases by sharing but not by saving. " \
                        "Please share this website with your friends and in your organization."
