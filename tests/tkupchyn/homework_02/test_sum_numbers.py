import pytest


def sum_numbers(string):
    return sum([int(num) for num in string.split() if num.isdigit()])


@pytest.mark.parametrize('string, num_sum', [
    ('This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year', 3755),
    ('This is th 1st string with the numbers 2 and 11', 13)
])
def test_sum_numbers(string, num_sum):
    assert sum_numbers(string) == num_sum
