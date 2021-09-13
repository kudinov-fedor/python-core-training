import pytest
import os


@pytest.fixture(scope="session")
def tmp_dir():
    path = os.path.join(os.getcwd(), "tmp")
    os.system("rm -rf {}".format(path))
    os.makedirs(path)
    yield path
    os.system("rm -rf {}".format(path))
