import pytest

TEST_STRING = "You know I'm born to lose, and gambling's for fools"

ER_1 = ['You', 'know', "I'm", 'born', 'to', 'lose,', 'and', "gambling's", 'for', 'fools']
ER_2 = ["You know I'm born to lose", "and gambling's for fools"]
ER_3 = ['You', 'know', "I'm born to lose, and gambling's for fools"]


@pytest.mark.parametrize('argument, result', [
    (None, ER_1),       # No arguments. Split using ' ' separator by default
    (", ", ER_2),       # ', ' as a separator
])
def test_split(argument, result):
    """
    Return a list of the words in the string, using sep as the delimiter string.
    Can be used without arguments or with sep
    """
    assert TEST_STRING.split(argument) == result


def test_split_with_args():
    """Can be used with and sep and maxsplit arguments"""
    TEST_STRING.split(' ', 2) == ER_3
