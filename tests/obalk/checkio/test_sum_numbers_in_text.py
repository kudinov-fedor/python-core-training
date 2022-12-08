import pytest
from obalk.checkio.sum_numbers_in_text import sum_numbers, sum_numbers_with_filter_map


@pytest.mark.parametrize("text, result", [
    ("hi", 0),
    ('who is 1st here', 0),
    ("""This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year""", 3755),
    ("", 0)
])
def test_sum_numbers(text, result):
    assert sum_numbers(text) == result


@pytest.mark.parametrize("text, result", [
    ("hi", 0),
    ('who is 1st here', 0),
    ("""This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year""", 3755),
    ("", 0)
])
def test_sum_numbers_with_filter_map(text, result):
    assert sum_numbers_with_filter_map(text) == result
