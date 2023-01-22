import pytest
from tlazu.Multiply import mult_two


@pytest.mark.parametrize("a, b, result", [
    (0, 2, 0),
    (2, 0, 0),
    (2, 3, 6),
    (6, 7, 42)
])
def test_mult_two(a, b, result):
    assert a, b == result