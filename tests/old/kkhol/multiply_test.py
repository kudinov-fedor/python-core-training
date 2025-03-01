from kkhol.multiply import multiply_two


import pytest


@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 6),
    (4, 2, 8),
    (0, 1, 0),
    (2, 1, 2)
])
def test_multiply_two(a, b, expected):
   assert multiply_two(a, b) == expected
