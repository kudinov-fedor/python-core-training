import pytest

from obalk.checkio.home.days_between import days_diff


@pytest.mark.parametrize("date_one, date_two, result", [
    ((1982, 4, 19), (1982, 4, 22), 3),
    ((2014, 8, 27), (2014, 1, 1), 238),
    ((2014, 1, 1), (2014, 8, 27), 238)
])
def test_duplicate_zeros(date_one, date_two, result):
    assert days_diff(date_one, date_two) == result
