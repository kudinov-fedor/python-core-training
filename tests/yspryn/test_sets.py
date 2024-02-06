def test_sets_union():
    test_set = {1, 45, 'abc', 'm', 'z'}
    assert test_set | ({45, 'K', 'm'}) == {1, 'K', 'abc', 'm', 'z', 45}
    assert test_set | {'45', 'mz', 1} == {1, 'abc', 'm', 'mz', 'z', '45', 45}
    assert test_set | {'m', 'mm'} == {1, 'abc', 'm', 'z', 'mm', 45}


def test_sets_intersection():
    assert {1, 'C', '23'} & {1, 'c', 23} == {1}
    assert {123, 'a', '1', 1}.intersection({1, 2, 3, 123}) == {1, 123}


def test_sets_difference():
    assert {1, 'C', '23', 'cc'} - {1, 'c', 23} == {'23', 'cc', 'C'}
    assert {1, 'C', '23', 'cc'} ^ {1, 'c', 23} == {'cc', 'C', 23, 'c', '23'}
