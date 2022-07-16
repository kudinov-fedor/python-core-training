from kkhol.int_length import number_length

import pytest


@pytest.mark.parametrize("b, number", [
    ('3', 1),
    ('4,902', 5),
    ('', 0)
])
def test_number_length(b, number):
    assert number_length(b) == number
