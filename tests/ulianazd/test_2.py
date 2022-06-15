import pytest


@pytest.fixture(scope='module')
def setup():
    return [7, 3]


def sum(a, b):
    return a + b


def test_sum(setup):
    assert sum(setup[0], setup[1]) == 10

