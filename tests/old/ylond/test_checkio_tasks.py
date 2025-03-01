import pytest


from ylond.checkio_tasks import backward_string, count_value, easy_unpack, end_zeros, extend_func, first_word, \
    is_acceptable_pass, isdigit_func, most_frequent, number_length


@pytest.mark.parametrize("text, expected", [
    (" ", " "),
    ("test", "tset"),
    ("1028564", "4658201"),
    ("okko", "okko")])
def test_backward_funct(text, expected):
    assert backward_string(text) == expected


@pytest.mark.parametrize("a, sub, expected", [
        ("", "test", 0),
        ("1 2 5 6 7 9 1 1 5 5", "5", 3),
        ("test1 test2 test3 test4", "test", 4)])
def test_count_funct(a, sub, expected):
    assert count_value(a, sub) == expected


@pytest.mark.parametrize("element, expected", [
            ((1, 0, 2, 3, 6, 7, 0), (1, 2, 7)),
            ((0, 7, 2, 8, 6, 7), (0, 2, 6)),
            ((1, 0, 2), (1, 2, 0)),
            ((1, 1, 2, 1), (1, 2, 2))])
def test_easy_unpack(element, expected):
    assert easy_unpack(element) == expected


@pytest.mark.parametrize("num, expected", [
    (10, 1),
    (222, 0),
    (10505000, 3),
    (0, 1)])
def test_end_zeros(num, expected):
    assert end_zeros(num) == expected


@pytest.mark.parametrize("a, b, expected", [
    ([1, 2, 4], [5, 6, 7], [1, 2, 4, 5, 6, 7]),
    ([], ['cat', 'dog'], ['cat', 'dog']),
    ([], (1, 2, 85), [1, 2, 85]),
    ([], {1, 'test', 85}, [1, 85, 'test']),
    ([], {'dict': 1, 'dict1': 2}, ['dict', 'dict1']),
    ([], range(10), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])])
def test_extend_funct(a, b, expected):
    assert extend_func(a, b) == expected


def test_extend_error():
    a = ('$', '100')
    b = [1, 2, 3]
    with pytest.raises(AttributeError):
         extend_func(a, b)


@pytest.mark.parametrize("text, expected", [
    ("", ""),
    ("1 2 5", "1"),
    ("-5e, exponent", "-5e,"),
    ("Hi Harry", "Hi"),
    ("NONE exception", "NONE"),
    ("First_word", "First_word")
])
def test_first_word(text, expected):
    assert first_word(text) == expected


@pytest.mark.parametrize("text, expected", [
    ("1 2 5 7", True),
    ("banana ", True),
    ("*******", True),
    ("", False),
    ("test", False),
    ("banana", False)
])
def test_accept_pass(text, expected):
    assert is_acceptable_pass(text) == expected


@pytest.mark.parametrize("txt, expected", [
    ("", False),
    ("1 2 5", False),
    ("0.1", False),
    ("\u00B2", True),
    ("\u0030", True),
    ("NULL", False),
    ("5000089999", True),
    ("-1", False)
])
def test_isdigit_funct(txt, expected):
    assert isdigit_func(txt) == expected


@pytest.mark.parametrize("a, expected", [
    (["a", "a", "b", "b", "c", "a"], "a"),
    ([1, 22, 22, 1, 100, 100], 1),
    (["A", "A", "a", "a"], "A")
])
def test_most_frequent(a, expected):
    assert most_frequent(a) == expected


@pytest.mark.parametrize("a, expected", [
    (0, 1),
    (44, 2),
    (5005005005, 10),
    ("", 0)
])
def test_number_length(a, expected):
    assert number_length(a) == expected
