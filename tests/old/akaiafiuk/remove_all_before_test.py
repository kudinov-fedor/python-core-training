from akaiafiuk.remove_all_before import remove_all_before


def test_remove_all_before():
    assert remove_all_before([1, 2, 3, 4, 5], 3) == [3, 4, 5]
    assert remove_all_before([1, 1, 2, 2, 3, 3], 2) == [2, 2, 3, 3]
    assert remove_all_before([1, 1, 2, 4, 2, 3, 4], 2) == [2, 4, 2, 3, 4]
    assert remove_all_before([1, 1, 5, 6, 7], 2) == [1, 1, 5, 6, 7]
    assert remove_all_before([], 0) == []
    assert remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
