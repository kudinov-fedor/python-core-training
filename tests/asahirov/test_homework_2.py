"""Дз:
 Написати тести які б перевіряли різні помилки в пайтоні наприклад:
5 / 0
assert False
list()[1000]
dict()["abc"]
int.foo


2. Спробувати покрити тестами ключові слова, наприклад:
not, and, or, in , is,  not in, is not
if elif else
for in
while
def
компрехеншни,
і тд."""
import pytest


def test_exception_zero_division():
    with pytest.raises(ZeroDivisionError):
        res = 999/0


def test_exception_assert():
    with pytest.raises(AssertionError):
        assert "soft" in "serve"


def test_exception_index():
    with pytest.raises(IndexError):
        example = [_*3 for _ in range(16)]
        _ = example[20]


def test_exception_key():
    with pytest.raises(KeyError):
        example = {"first": 1, "second": 2}
        _ = example["third"]


def test_exception_attribute():
    with pytest.raises(AttributeError):
        _ = int.foo


def test_if_else_while():
    list_object = [1, 2, 3, 4, "qwe", [1, 4, 5]]
    while list_object:
        if list_object:
            list_object.pop(-1)
        else:
            assert list_object is False

    assert len(list_object) == 0
