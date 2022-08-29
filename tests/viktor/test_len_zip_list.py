import pytest


@pytest.fixture(scope='module')
def setup():
    return [5, 3]


def sum(a, b):
    return a + b


@pytest.mark.xfail
def test_sum_error(setup):
    assert sum(setup[0], setup[1]) == 7


def test_positive_sum(setup):
    assert sum(setup[0], setup[1]) == 8


def test_check_error(setup):
    with pytest.raises(TypeError):
        sum(setup)


def test_sum_simple():
    assert (2 + 3) == 5


@pytest.mark.parametrize('a, b, c', [
    (1, 2, 3),
    (4, 5, 9),
    (7, 8, 15),
    ('st', 'df', 'stdf'),
    ((1, 2, 3), (4, 5, 9), (1, 2, 3, 4, 5, 9)),
    ([3, 4, 'c'], ['v', 's', 5], [3, 4, 'c', 'v', 's', 5]),
    ((1,), (), (1,)),
    ([], [3], [3])
])
def test_sum_simple_parametrize(a, b, c):
    assert (a + b) == c
