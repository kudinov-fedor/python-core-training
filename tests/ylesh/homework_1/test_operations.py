import pytest

mylist = [1, 2, 3, 4, 5, 6, 7, 8]


@pytest.mark.parametrize(["param", "result"], [
    (list(filter(lambda x: x % 2 == 0, mylist)) == [2, 4, 6, 8], True),
    ([3, 8] + [3, 8] == [3, 8, 3, 8], True),
    ((pow(5, 3)) - (sum([100, 7, 3])), 15),
    ((divmod(6, 2)) == (3, 0), True)
])
def test_assertion(param, result):
    assert param is result
