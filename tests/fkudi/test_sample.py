import pytest


def test_sample():
    assert 1 == 1


def test_pass():
    pass


@pytest.mark.xfail
def test_error():
    res = 1 != 1
    print(res)
    assert res


@pytest.mark.parametrize("param1, param2, res", [
    (5, 2, 2.5),  # pos / pos
    (-4, 2, -2),  # neg / neg
    (0, 4, 0),    # zero divide
])
def test_division(param1, param2, res):
    assert param1 / param2 == res


def test_my_len():
    # arrange
    item = [1, 2, 3]

    # act
    res = len(item)

    # assert
    assert res == 3
