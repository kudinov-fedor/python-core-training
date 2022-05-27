# test built-in functions len/zip/enumarate
import pytest


@pytest.mark.parametrize("param, res", [
    ("test", 4),
    ("0123654", 7),
    ("", 0)])
def test_len(param, res):
    len(param) == res


def test_len_error():
    param = 123456
    with pytest.raises(TypeError):
        len(param)


@pytest.mark.parametrize("set1, set2, res", [
    ((1, 3, 5), ("Apple", "Orange", "Pamelo"), [(1, "Apple"), (3, "Orange"), (5, "Pamelo")]),
    ([], [], []),
    ((1, 2), ["x", "y", "z"], [(1, "x"), (2, "y")]) ])
def test_zip(set1, set2, res):
    print(list(zip(set1, set2))) == res
