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
        999/0


def test_exception_assert():
    with pytest.raises(AssertionError):
        assert "soft" in "serve"


def test_exception_index():
    # code created in this way to practice more with comprehension
    example = [item * 3 for item in range(16)]
    with pytest.raises(IndexError):
        example[20]


def test_exception_key():
    example = {"first": 1, "second": 2}
    with pytest.raises(KeyError):
        example["third"]


def test_exception_attribute():
    with pytest.raises(AttributeError):
        int.foo


def test_if_else_while():
    list_object = [1, 2, 3, 4, "qwe", [1, 4, 5]]
    while len(list_object) != 0:
        list_object.pop()
        if not list_object:
            assert list_object == []
        else:
            assert len(list_object) > 0
    assert len(list_object) == 0
