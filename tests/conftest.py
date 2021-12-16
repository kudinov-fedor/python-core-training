import pytest
import os

from selenium_helpers.session import create_session
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="session")
def tmp_dir():
    path = os.path.join(os.getcwd(), "tmp")
    os.system("rm -rf {}".format(path))
    os.mkdir(path)
    yield path
    os.system("rm -rf {}".format(path))


@pytest.fixture(scope="session")
def session() -> WebDriver:
    session = create_session()
    yield session
    session.quit()
