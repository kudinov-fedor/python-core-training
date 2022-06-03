# test built-in functions len/zip/enumerate
import pytest


@pytest.mark.parametrize("param, res", [
    ("test", 4),
    ("0123654", 7),
    ("", 0)])
def test_len(param, res):
    assert len(param) == res


def test_len_error():
    param = 123456
    with pytest.raises(TypeError):
        len(param)


@pytest.mark.parametrize("set1, set2, res", [
    ((1, 3, 5), ("Apple", "Orange", "Pamelo"), [(1, "Apple"), (3, "Orange"), (5, "Pamelo")]),
    ([], [], []),
    ((1, 2), ["x", "y", "z"], [(1, "x"), (2, "y")])])
def test_zip(set1, set2, res):
    assert list(zip(set1, set2)) == res


@pytest.mark.parametrize("list1, res", [
    ((1, 3, 5), [(0, 1), (1, 3), (2, 5)]),
    (["b", "a", "c"], [(0, 'b'), (1, 'a'), (2, 'c')]),
    ((), [])])
def test_enumerate(list1, res):
    assert list(enumerate(list1)) == res
