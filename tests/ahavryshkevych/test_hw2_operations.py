import pytest


def test_round_function():
    number = round(4.345)
    assert type(number) is not float


def test_round_float_digits():
    my_float = round(4.345, 1)
    count_after_comma = str(my_float)[::-1].find('.')
    assert count_after_comma == 1


@pytest.mark.parametrize(["par", "result"], [
    ([1, 2, 3], 6),
    ((1, 2, 3), 6),
    ({1, 2, 3}, 6)
])
def test_number_sequence_sum(par, result):
    res = sum(par)
    assert res is result
