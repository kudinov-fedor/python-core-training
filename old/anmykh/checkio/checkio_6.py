# This function should take two positive numbers (length and width) as inputs and return the perimeter of a rectangle.
import pytest


def rectangle_perimeter(length: int, width: int) -> int:
    perimeter = (length + width) * 2
    return perimeter


@pytest.mark.parametrize(["length", "width", "result"], [
    [5, 3, 16],
    [7, 4, 22],
    [10, 20, 60],
    [7, 2, 18]
])
def test_rectangle_perimeter(length, width, result):
    assert rectangle_perimeter(length, width) == result
