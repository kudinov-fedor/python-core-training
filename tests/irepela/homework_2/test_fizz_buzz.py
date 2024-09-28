import pytest
from irepela.homework_2.fizz_buzz import fizz_buzz


@pytest.mark.parametrize("arg, expected", [
    (15, "Fizz Buzz"),
    (6, "Fizz"),
    (10, "Buzz"),
    (7, "7"),
])
def test_fizz_buzz(arg, expected):
    assert fizz_buzz(arg) == expected
