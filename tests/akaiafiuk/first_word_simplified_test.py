from akaiafiuk.first_word_simplified import first_word, first_word_using_split


def test_first_word():
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"


def test_first_word_using_split():
    assert first_word_using_split("Hello world") == "Hello"
    assert first_word_using_split("a word") == "a"
    assert first_word_using_split("hi") == "hi"
