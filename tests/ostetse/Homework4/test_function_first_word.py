import pytest

from tests.ostetse.Homework4.function_first_word import first_word


def test_first_word():
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("greeting from CheckiO Planet") == "greeting"
    assert first_word("hi") == "hi"
