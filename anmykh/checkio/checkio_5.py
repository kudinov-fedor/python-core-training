# Write a function that will receive 2 numbers as input and it should return the multiplication of these 2 numbers.

import pytest


def multiply(item1, item2):
    return item1 * item2


@pytest.mark.parametrize(["item1", "item2", "result"], [
    [1, 2, 2],
    [3.5, 6.7, 23.45],
    [32000, 323223, 10343136000]
])
def test_multiply(item1, item2, result):
    assert multiply(item1, item2) == result
