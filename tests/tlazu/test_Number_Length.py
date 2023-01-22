import pytest
from tlazu.Number_Length import number_length


@pytest.mark.parametrize("function", [number_length])
@pytest.mark.parametrize("value, result", [
    (10, 2),
    (0, 1),
    (1, 1),
    (44, 2)
])
def test_number_length(function, value, result):
    assert function(value) == result