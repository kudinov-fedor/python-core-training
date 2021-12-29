import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from .constants import CAPABILITIES
from selenium_helpers.session import create_session


@pytest.fixture(scope="session", params=CAPABILITIES)
def capabilities(request):
    return request.param


@pytest.fixture(scope="session")
def session(capabilities) -> WebDriver:
    session = create_session(config=capabilities)
    session.implicitly_wait(0.5)
    yield session
    session.quit()


@pytest.fixture()
def take_screen_on_fail(session, request):
    yield
    if request.node.rep_call.outcome == "failed":
        session.save_screenshot("{}.png".format(request.node.name))
