import pytest
from ahavryshkevych.task_three_words import three_words


@pytest.mark.parametrize(["arg1", "res"], [
    ("Hello World hello", True),
    ("He is 123 man", False),
    ("1 2 3 4", False),
    ("bla bla bla bla", True),
    ("Hi", False)
])
def test_three_words(arg1, res):
    assert three_words(arg1) == res
