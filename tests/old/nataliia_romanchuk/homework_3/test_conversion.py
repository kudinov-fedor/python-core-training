import pytest


def test_int_conversion():
    # Конвертація у ціле число (int)
    assert int("123") == 123
    assert int(123.0) == 123
    # Конвертація з різних систем числення (двійкова база = 2)
    assert int("10110101", 2) == 181
    assert int("0b10110101", 2) == 181


def test_float_conversion():
    # Конвертація у число з плаваючою крапкою (float)
    assert float("123") == 123.0
    assert float(123.0) == 123.0
    assert float(123) == 123.0


def test_str_conversion():
    # Конвертація у рядок (str)
    assert str(123) == "123"
    assert str(123.0) == "123.0"
    assert str(True) == "True"
    assert str(None) == "None"


def test_list_conversion():
    # Конвертація у списки (list)
    assert list("abc") == ["a", "b", "c"]
    assert list({"a": 1, "b": 2}) == ["a", "b"]  # Словник повертає ключі
    assert list((1, 2, 3)) == [1, 2, 3]

    # Множини (set) не мають порядку, тому перевіряємо через sorted або set
    assert set(list({"a", "b"})) == {"a", "b"}

    assert list(range(10)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(enumerate(["a", "b", "c"])) == [(0, "a"), (1, "b"), (2, "c")]
    assert list(zip(["a", "b", "c"], [1, 2, 3])) == [("a", 1), ("b", 2), ("c", 3)]

    # Робота з методами словника
    assert list({"a": 1, "b": 2}.keys()) == ["a", "b"]
    assert list({"a": 1, "b": 2}.values()) == [1, 2]
    assert list({"a": 1, "b": 2}.items()) == [("a", 1), ("b", 2)]


def test_tuple_and_set_conversion():
    # Конвертація у кортежі (tuple) та множини (set)
    assert tuple("abc") == ("a", "b", "c")
    assert tuple({"a": 1, "b": 2}) == ("a", "b")
    assert tuple((1, 2, 3)) == (1, 2, 3)
    assert set(tuple({"a", "b"})) == {"a", "b"}

    assert set("abc") == {"a", "b", "c"}
    assert set({"a": 1, "b": 2}) == {"a", "b"}
    assert set((1, 2, 3)) == {1, 2, 3}


def test_dict_conversion():
    # Створення словників (dict) різними способами
    expected = {"a": 123, "b": 456}
    assert dict(a=123, b=456) == expected
    assert dict([("a", 123), ("b", 456)]) == expected
    assert dict({"a": 1, "b": 2}) == {"a": 1, "b": 2}

    # dict з enumerate та zip
    assert dict(enumerate(["a", "b", "c"])) == {0: "a", 1: "b", 2: "c"}
    assert dict(zip(["a", "b", "c"], [1, 2, 3])) == {"a": 1, "b": 2, "c": 3}
    assert dict({"a": 1, "b": 2}.items()) == {"a": 1, "b": 2}
