from tests.ostetse.Homework4.define_function_fizz_buzz import checkio


def test_checkio():
    assert checkio(15) == "Fizz Buzz"
    assert checkio(6) == "Fizz"
    assert checkio(10) == "Buzz"
    assert checkio(7) == "7"
