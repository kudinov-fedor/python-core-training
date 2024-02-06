import pytest


@pytest.mark.parametrize(["item", "output"],
                         [("abc", ["a", "b", "c"])])
def test_list(item, output):
    assert list(item) == output


def test_empty():
    assert int() == 0
    assert bool() == False
    assert float() == 0.0
    assert str() == ''
    assert tuple() == ()
    assert list() == []
    assert range(10) == range(0, 10, 1)
    assert set() != ()
    assert dict() == {}


def test_is():
    assert [1, 2, 3] == [1, 2, 3]
    assert [1, 2, 3] is not [1, 2, 3]
