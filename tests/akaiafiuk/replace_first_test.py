from akaiafiuk.replace_first import replace_first, replace_last


def test_replace_first():
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []


def test_replace_last():
    assert list(replace_last([1, 2, 3, 4])) == [4, 1, 2, 3, ]
    assert list(replace_last([1])) == [1]
    assert list(replace_last([])) == []
