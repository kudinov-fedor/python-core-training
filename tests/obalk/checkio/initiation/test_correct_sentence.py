import pytest

from obalk.checkio.initiation.correct_sentence import correct_sentence


@pytest.mark.parametrize("function", [
    correct_sentence,
])
@pytest.mark.parametrize("text, result", [
    ("welcome to New York", "Welcome to New York."),
    ("Greetings, friends", "Greetings, friends."),
    ("greetings, friends", "Greetings, friends."),
    ("greetings, friends.", "Greetings, friends."),
    ("Greetings, friends.", "Greetings, friends.")
])
def test_end_zeros(function, text, result):
    assert function(text) == result
