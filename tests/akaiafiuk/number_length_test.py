from akaiafiuk.number_length import number_length
import pytest


@pytest.mark.parametrize("number, result", [
    (10, 2),
    (0, 1),
    (4, 1),
    (44, 2)
])
def test_number_length(number, result):
    assert number_length(number) == result
