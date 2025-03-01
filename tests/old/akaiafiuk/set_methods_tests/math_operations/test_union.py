s = {1, 2, 3, 4}
z = {2, 3, 5}
y = {7, 8, 9}


def test_or():
    """Test union using operator"""
    x = s | z
    assert x == {1, 2, 3, 4, 5}


def test_intersection_using_union():
    """Can intersect multiple sets at once using union()"""
    x = s.union(y, z)
    assert s == {1, 2, 3, 4}
    assert x == {1, 2, 3, 4, 5, 7, 8, 9}
