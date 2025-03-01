import pytest


@pytest.mark.parametrize(["param1", "param2"], [
    (5, 0)
])
def test_assertion1(param1, param2):
    try:
        param1 / param2
    except ZeroDivisionError as error:
        assert isinstance(error, ZeroDivisionError)


@pytest.mark.parametrize(["param", "result"], [
    (type(False) == bool, True),
    (type([1, 3]) == list, True),
    (type((1, 2, 5)) == tuple, True),
    (type({0: "a", 1: "b"}) == dict, True),
    (isinstance(False, (int, float, str)), True),
    (issubclass(bool, float), False),
    (hasattr([1, 3, 6], "append"), True)
])
def test_assertion2(param, result):
    assert param is result
