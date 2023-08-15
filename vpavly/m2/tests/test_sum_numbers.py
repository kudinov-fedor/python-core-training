import pytest

from vpavly.m2.sum_numbers import sum_numbers_lambda


@pytest.mark.parametrize('a, expected', [
    ('hi', 0),
    ('my numbers is 2', 2),
    ('This picture is an oil on canvas '
     'painting by Danish artist Anna '
     'Petersen between 1845 and 1910 year', 3755),
    ('5 plus 6 is', 11),
    ('', 0)
])
def test_sum_numbers(a, expected):
    assert sum_numbers_lambda(a) == expected
