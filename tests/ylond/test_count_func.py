import pytest

from ylond.count_func import count_value


@pytest.mark.parametrize("a, sub, expected", [
    ("", "test", 0),
    ("1 2 5 6 7 9 1 1 5 5", "5", 3),
    ("test1 test2 test3 test4", "test", 4)])
def test_count_funct(a, sub, expected):
    assert count_value(a, sub) == expected
