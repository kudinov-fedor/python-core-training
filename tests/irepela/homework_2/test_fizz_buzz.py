from irepela.homework_2.fizz_buzz import checkio


def test_fizz_buzz():
    assert checkio(15) == "Fizz Buzz"
    assert checkio(6) == "Fizz"
    assert checkio(10) == "Buzz"
    assert checkio(7) == "7"
