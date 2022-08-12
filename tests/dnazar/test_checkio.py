import pytest
import dnazar.checkio_tasks as checkio


@pytest.mark.parametrize("item, expected_word", [
    (" ", ""),
    ("Hello", "Hello"),
    ("Hello world", "Hello"),
    ("a word", "a"),
    ("greeting from CheckiO Planet", "greeting"),
    ("    hi       ", "hi"),
    ("      first           word          ", "first"),
    ("      1", "1"),
    (",*]|[, ,{].", ",*]|[,")
])
def test_first_word(item, expected_word):
    assert checkio.first_word(item) == expected_word


@pytest.mark.parametrize("item", [
    ["some", "values", "here"],
    (1, 2, 3),
    323,
    True])
def test_first_word_error(item):
    with pytest.raises(TypeError):
        checkio.first_word(item)


@pytest.mark.parametrize("item, expected", [
    (["a", "b", "c", "a", "a", "b"], "a"),
    (["a", "b", "c", "a", "c", "b"], "a, b, c"),
    (["aa", "a", "aaa", "ab", "aa", "ba"], "aa"),
    ([",", ".", "aaa", ",", ".", "ba"], ",, .")
])
def test_most_frequent(item, expected):
    assert checkio.most_frequent(item) == expected


@pytest.mark.parametrize("item", [
    "text",
    123,
    (1, 2, 3),
    False,
    [1, 2, 3, 2, 2, 3],
    ["1", 2, True, "2", 1, True, 1]
])
def test_most_frequent_error(item):
    with pytest.raises(TypeError):
        checkio.most_frequent(item)

@pytest.mark.parametrize("item, expected", [
    (["a", "b", "c", "a", "a", "b"], "a"),
    (["a", "b", "c", "a", "c", "b"], "a"),
    (["c", "b", "c", "a", "a", "b"], "c"),
    (["aa", "a", "aaa", "ab", "aa", "ba"], "aa"),
    ([",", ".", "aaa", ",", ".", "ba"], ",")
])
def test_most_frequent_with_max(item, expected):
    assert checkio.most_frequent_with_max(item) == expected


@pytest.mark.parametrize("item, expected", [
    (["a", "b", "c", "a", "a", "b"], ["a"]),
    (["a", "b", "c", "a", "c", "b"], ["a", "b", "c"]),
    (["aa", "a", "aaa", "ab", "aa", "ba"], ["aa"]),
    ([",", ".", "aaa", ",", ".", "ba"], [",", "."])
])
def test_most_frequent_with_dict(item, expected):
    assert checkio.most_frequent_with_dict(item) == expected
