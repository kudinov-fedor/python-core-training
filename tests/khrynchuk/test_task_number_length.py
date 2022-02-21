import pytest

from khrynchuk.task_number_length import number_length


@pytest.mark.parametrize("number, length", [
    (13, 2),
    (1245, 4),
    (6765837465, 10),
])
def test_number_length(number, length):
    assert number_length(number) == length
