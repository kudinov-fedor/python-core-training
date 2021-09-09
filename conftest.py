import pytest
import os

from helpers.session import create_session


@pytest.fixture(scope="session")
def session():
    session = create_session()
    yield session
    session.close()


@pytest.fixture(scope="session")
def tmp_dir():
    path = os.path.join(os.getcwd(), "tmp")
    os.system("rm -rf {}".format(path))
    os.makedirs(path)
    yield path
    os.system("rm -rf {}".format(path))
