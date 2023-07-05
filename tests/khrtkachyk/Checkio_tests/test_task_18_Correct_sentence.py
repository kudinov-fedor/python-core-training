import pytest
from checkio_tasks.task_18_Correct_sentence import correct_sentence, correct_sentence_2_0


"""
For the input of your function, you will be given one sentence.
You have to return a corrected version, that starts with a capital letter and ends with a period (dot).

Pay attention to the fact that not all the fixes are necessary.
If a sentence already ends with a period (dot), then adding another one will be a mistake.

Input: A string (str).
Output: A string (str).

Precondition: No leading and trailing spaces, text contains only spaces, a-z, A-Z, "," and ".".
"""


@pytest.mark.parametrize("func", [correct_sentence, correct_sentence_2_0])
@pytest.mark.parametrize("sentence, res", [
    ("greetings, friends", "Greetings, friends."),
    ("Greetings, friends", "Greetings, friends."),
    ("Greetings, friends.", "Greetings, friends."),
    ("greetings, friends.", "Greetings, friends."),
    ("hi", "Hi."),
    ("welcome to Lviv city", "Welcome to Lviv city.")
])
def test_correct_sentence(func, sentence, res):
    assert func(sentence) == res
