import pytest


def fizz_buzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


@pytest.mark.parametrize('n, expected_result', [
    (1, '1'),
    (2, '2'),
    (3, 'Fizz'),
    (5, 'Buzz'),
    (15, 'FizzBuzz')])
def test_fizz_buzz(n, expected_result):
    assert fizz_buzz(n) == expected_result
