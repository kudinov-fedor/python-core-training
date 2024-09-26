from irepela.homework_2.three_words import checkio


def test_three_words():
    assert checkio("Hello World hello") is True
    assert checkio("He is 123 man") is False
    assert checkio("1 2 3 4") is False
    assert checkio("bla bla bla bla") is True
    assert checkio("Hi") is False
    assert checkio('one two 3 four five six 7 eight 9 ten eleven 12') is True
