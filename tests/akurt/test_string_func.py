import pytest


@pytest.mark.str
@pytest.mark.parametrize("input, expected", [
    ("hi", "HI"),
    ("anna", "ANNNA")
])
def test_upper(input, expected):
    assert input.upper() == expected


@pytest.mark.str
@pytest.mark.parametrize("a, b, c, expected", [
    ("aaaaa", "a", "b", "bbbbb"),
    ("anna", "a", "j", "jnna")
])
def test_replace(a, b, c, expected):
    assert a.replace(b, c) == expected


@pytest.mark.str
@pytest.mark.parametrize("a, b, expected", [
    ("Hello, world", ",", ['Hello', ' world']),
    ("12345 + kat + mouse", "+", ['12345 ', ' kat ', ' mouse'])
])
def test_split(a, b, expected):
    assert a.split(b) == expected


@pytest.mark.str
@pytest.mark.parametrize("a, b, expected", [
    ("Hello", " world", "Hello world")
])
def test_conc(a, b, expected):
    assert a + b == expected


@pytest.mark.str
@pytest.mark.parametrize("a, b, expected", [
    ("Hello", "world", "Hello world")
])
def test_conc_fail(a, b, expected):
    assert a + b != expected


@pytest.mark.str
@pytest.mark.parametrize("a, b, expected", [
    ("Anna likes rum, Ihor likes rum too", "rum", 2),
    ("Anna likes rum, Ihor likes rum too", "Anna", 1),
    ("Anna likes rum, Ihor likes rum too", "likes", 2)
])
def test_count(a, b, expected):
    assert a.count(b) == expected


@pytest.mark.str
@pytest.mark.parametrize("a, q, i, p, expected", [
    ("I want to pay {2} dollars for {0} pieces of item {1}", "2", "6", "1",
     "I want to pay 1 dollars for 2 pieces of item 6"),
    ("I want to pay {2} dollars for {0} pieces of item {1}", 2, 6, 1, "I want to pay 1 dollars for 2 pieces of item 6")
])
def test_format(a, q, i, p, expected):
    assert expected.format(q, i, p) == expected

@pytest.mark.str
@pytest.mark.parametrize("a, b, c, expected", [
    ("I want to pay 2 dollars for 6 pieces of item 1", 0, 5, "I wan"),
    (" I want to pay 2 dollars for 6 pieces of item 1", -6, -2, "item")
])
def test_slice(a, b, c, expected):
    assert a[b:c] == expected

@pytest.mark.str
@pytest.mark.parametrize("a, expected", [
    (" I want to pay 2 dollars for 6 pieces of item 1 ", "I want to pay 2 dollars for 6 pieces of item 1")
])
def test_strip(a, expected):
    assert a.strip() == expected
