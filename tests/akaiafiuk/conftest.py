import pytest


@pytest.fixture(scope='function')
def test_list():
    return [1, 2, 3]
