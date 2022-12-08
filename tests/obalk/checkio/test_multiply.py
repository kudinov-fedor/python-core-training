import pytest
from obalk.checkio.multiply import mult_two


@pytest.mark.parametrize(
    "number1, number2, result", [
        (0, 2, 0),
        (2, 0, 0),
        (2, 3, 6),
        (6, 7, 42)
    ]
)
def test_mult_two(number1, number2, result):
    assert mult_two(number1, number2) == result
