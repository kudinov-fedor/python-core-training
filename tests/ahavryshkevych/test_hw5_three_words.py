import pytest
from ahavryshkevych.task_three_words import three_words, three_words02, three_words03


@pytest.mark.parametrize(["arg1", "res"], [
    ("Hello World hello", True),
    ("He is 123 man", False),
    ("1 2 3 4", False),
    ("bla bla bla bla", True),
    ("Hi", False)
])
def test_three_words(arg1, res):
    assert three_words(arg1) == res


@pytest.mark.parametrize(["arg1", "res"], [
    ("Hello World hello", True),
    ("He is 123 man", False),
    ("1 2 3 4", False),
    ("bla bla bla bla", True),
    ("Hi", False)
])
def test_three_words02(arg1, res):
    assert three_words02(arg1) == res


@pytest.mark.parametrize(["arg1", "res"], [
    ("Hello World hello", True),
    ("He is 123 man", False),
    ("1 2 3 4", False),
    ("bla bla bla bla", True),
    ("Hi", False)
])
def test_three_words3(arg1, res):
    assert three_words03(arg1) == res