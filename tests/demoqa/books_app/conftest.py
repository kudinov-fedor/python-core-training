import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from .constants import BROWSERS, SIZES, WINDOW_PREFS
from selenium_helpers.session import create_session


@pytest.fixture(scope="session", params=SIZES)
def size(request):
    return request.param


@pytest.fixture(scope="session", params=BROWSERS)
def browser(request):
    return request.param


@pytest.fixture(scope="session")
def session(size, browser) -> WebDriver:
    session = create_session(browser)
    if size == "L":
        if WINDOW_PREFS.get("L"):
            session.set_window_size(*WINDOW_PREFS["L"])
        else:
            session.maximize_window()
    elif size == "M":
        if WINDOW_PREFS.get("M"):
            session.set_window_size(*WINDOW_PREFS["M"])
    elif size == "S":
        if WINDOW_PREFS.get("S"):
            session.set_window_size(*WINDOW_PREFS["S"])

    yield session
    session.quit()
