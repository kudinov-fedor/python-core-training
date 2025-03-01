import pytest
from irepela.homework_2.multiply import mult_two


@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (3, 2, 6),
    (0, 1, 0),
])
def test_multiply(a, b, expected):
    assert mult_two(a, b) == expected
