import pytest


@pytest.fixture(scope='module')
def setup():
    return [5, 3]


def sum(a, b):
    return a + b


@pytest.mark.xfail
def test_sum(setup):
    assert sum(setup[0], setup[1]) == 7