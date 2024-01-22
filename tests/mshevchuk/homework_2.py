import pytest


# Дз:
#  Написати тести які б перевіряли різні помилки в пайтоні наприклад:
# 5 / 0
# assert False
# list()[1000]
# dict()["abc"]
# int.foo
#
#
# 2. Спробувати покрити тестами ключові слова, наприклад:
# not, and, or, in , is,  not in, is not
# if elif else
# for in
# while
# def
# компрехеншни,
# і тд.

def test_zero_division_exception():
    with pytest.raises(ZeroDivisionError):
        res = 0 / 0


def test_types_exception():
    i = (1, 1)
    with pytest.raises(IndexError):
        print(i[2])


def test_assertion_error():
    with pytest.raises(AssertionError):
        assert True == False is False


def test_key_error():
    student = {
        'name': 'John',
        'age': 20,
        'grade': 'A'
    }
    with pytest.raises(KeyError):
        student["surname"]


def test_name_error():
    with pytest.raises(AttributeError):
        str.some_attribute


def is_even(number):
    return number % 2 == 0


def test_not_even():
    assert not is_even(3), "3 should not be even"


def test_even():
    assert is_even(4), "4 should be even"


def test_not_false():
    assert (not False) == True, "should be even"


def test_not_true():
    assert (not True) == False, "should be even"


def test_if():
    if True:
        assert True
    else:
        raise AssertionError("else should not be reachable")


def test_if_2():
    if False:
        raise AssertionError("If should not be reachable")
    else:
        assert True


def test_for_for():
    fibo = [0, 1, 1, 2, "Some text", -3, 5, 8, 13]
    first = fibo[0]
    second = fibo[1]
    for i in range(1, len(fibo)):
        if isinstance(fibo[i], int):
            assert first + second == abs(fibo[i])
            second = abs(first)
            first = abs(fibo[i])
