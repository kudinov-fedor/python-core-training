a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
b = {1, 2, 3}
c = {7, 8, 9}
d = {'a', 'b', 'c'}


def test_subtraction_operator():
    """Test subtraction (difference) using operator"""
    x = a - b
    assert x == {4, 5, 6, 7, 8, 9}


def test_subtraction_operator_empty_set():
    """
    Test when all elements are removed as a result of subtraction.
    Note that set() and not {} is returned
    """
    x = b - a
    assert x != {}
    assert x == set()


def test_subtraction_operator_no_common():
    """First set is returned when there's no common elements during subtraction"""
    x = a - d
    assert x == a


def test_subtract_using_method():
    """difference() method can be used to subtract multiple sets"""
    x = a.difference(b, c, d)
    assert a == {1, 2, 3, 4, 5, 6, 7, 8, 9}
    assert x == {4, 5, 6}


def test_subtract_using_method_empty_result():
    """difference() method when all elements are removed"""
    x = b.difference(a, c, d)
    assert x == set()


def test_subtract_using_method_no_common():
    """difference() does not change original set when there's no common elements"""
    x = d.difference(a, b, c)
    assert x == {'c', 'a', 'b'}


def test_in_place_difference_operator():
    """-= changes the original set"""
    x = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    y = {1, 2, 3}
    x -= y
    assert x == {4, 5, 6, 7, 8, 9}


def test_in_place_difference_method():
    """difference_update() changes the original set"""
    x = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    y = {1, 2, 3}
    z = {7, 8, 9}
    x.difference_update(y, z)
    assert x == {4, 5, 6}
