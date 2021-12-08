import pytest


@pytest.mark.parametrize("data, expected", [
    (23, int),
    ('test', str),
    (True, bool),
    (0.5, float),
    ([1, 2, 3], list),
    ({1: 'one', 2: False, 3: 123}, dict)
])
def test_type(data, expected):
    assert type(data) == expected


@pytest.mark.parametrize("data, expected", [
    ('2 + 2', 4),
    ('11 - 33', -22),
    (2 - 2, 0)
])
def test_eval(data, expected):
    try:
        assert eval(data) == expected
    except TypeError:
        print('There is a wrong data type(integer)')
