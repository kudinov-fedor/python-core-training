import pytest
from tkupchyn.homework_02.fizz_buzz import fizz_buzz


@pytest.mark.parametrize('n, expected_result', [
    (1, '1'),
    (2, '2'),
    (3, 'Fizz'),
    (5, 'Buzz'),
    (15, 'FizzBuzz'),
    (330, 'FizzBuzz')])
def test_fizz_buzz(n, expected_result):
    assert fizz_buzz(n) == expected_result
