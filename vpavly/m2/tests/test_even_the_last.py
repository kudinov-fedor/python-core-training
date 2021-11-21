import pytest

from vpavly.m2.even_the_last import even_last


@pytest.mark.parametrize('a, expected', [
    ([0, 1, 2, 3, 4, 5], 30),
    ([1, 3, 5], 30),
    ([6], 36),
    ([], 0)
])
def test_even_last(a, expected):
    assert even_last(a) == expected
