import pytest
import os

from selenium_helpers.session import create_session
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture(scope="session")
def tmp_dir():
    path = os.path.join(os.getcwd(), "tmp")
    os.system("rm -rf {}".format(path))
    try:
        os.makedirs(path)
    except FileExistsError:
        ...
    yield path
    os.system("rm -rf {}".format(path))


@pytest.fixture(scope="session")
def session() -> WebDriver:
    session = create_session()
    yield session
    session.quit()
