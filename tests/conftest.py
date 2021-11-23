import pytest
import os

from selenium_helpers.session import create_session


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
def session():
    session = create_session()
    yield session
    session.close()
