import pytest

from ihontaryk.home_work_2 import fizz_buzz, multiply_numbers, sum_numbers


@pytest.mark.parametrize("number, expected_result",
                         [(1, "1"),
                          (3, "Fizz"),
                          (5, "Buzz"),
                          (-15, "FizzBuzz"),
                          (0, "0")])
def test_fizz_buzz_positive(number, expected_result):
    """verify positive scenarios for fizz_buss function"""
    assert fizz_buzz(number) == expected_result


@pytest.mark.parametrize("number, error",
                         [(0, ValueError),
                          (1.5, TypeError),
                          ("abc", TypeError),
                          (False, TypeError),
                          ([1, 2, 3], TypeError),
                          ({1, 2, 3}, TypeError)
                          ])
def test_fizz_buzz_negative(number, error):
    """verify negative scenarios for fizz_buss function"""
    with pytest.raises(error):
        fizz_buzz(number)


@pytest.mark.parametrize("number1, number2,  expected_result",
                         [(0, 2, 0),
                          (2, 5, 10),
                          (-5, -5, 25),
                          (-50, 2, -100)
                          ])
def test_multiply_numbers_positive(number1, number2, expected_result):
    """verify positive scenarios for multiply_numbers function"""
    assert multiply_numbers(number1, number2) == expected_result


@pytest.mark.parametrize("number1, number2,  error",
                         [("abc", 2, TypeError),
                          (False, 1, TypeError),
                          (4, [1, 2, 3], TypeError),
                          (8, {1, 2, 3}, TypeError)
                          ])
def test_multiply_numbers_negative(number1, number2, error):
    """verify negative scenarios for multiply_numbers function"""
    with pytest.raises(error):
        multiply_numbers(number1, number2)


@pytest.mark.parametrize("text, expected_result",
                         [("Today is 27.09. Yesterday was 26th of September. 27 is greater than 26", 53)
                          ])
def test_sum_numbers(text, expected_result):
    """verify positive scenarios for sum_numbers function"""
    assert sum_numbers(text) == expected_result
