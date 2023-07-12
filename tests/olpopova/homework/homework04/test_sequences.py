import pytest


@pytest.mark.parametrize(['col1', 'col2', 'expected'], [
    (("c", "a", "t"), ("d", "o", "g"), ("c", "a", "t", "d", "o", "g")),
    ([5, 6, 4], [3, 7, 9], [5, 6, 4, 3, 7, 9])
])
def test_sum_collections(col1, col2, expected):
    assert col1 + col2 == expected


@pytest.mark.parametrize(['seq1', 'seq2', 'expected'], [
    ('Hello', ' World', (False, False)),
    ([1, 2, 3], [4, 5, 6], (True, True)),
    (('a', 'b', 'c'), ('f', 'h', 'o'), (False, False))
])
def test_inplace_operation(seq1, seq2, expected):
    a = seq1
    b = a
    a += seq2
    assert (a == b, a is b) == expected


@pytest.mark.parametrize(['param', 'expected'], [
    (2, (1, 3, 5, 7, 9)),
    (-1, (9, 8, 7, 6, 5, 4, 3, 2, 1)),
    (None, (1, 2, 3, 4, 5, 6, 7, 8, 9))
])
def test_string_slicing(param, expected, sequence=(1, 2, 3, 4, 5, 6, 7, 8, 9)):
    assert (sequence[param:param] if param is None else sequence[::param]) == expected


@pytest.mark.parametrize(['start', 'end', 'step', 'expected'], [
    (None, 7, 2, (1, 3, 5, 7)),
    (0, 7, 2, (1, 3, 5, 7)),
    (1, 7, 2, (2, 4, 6))
])
def test_slicing_with_params(start, end, step, expected):
    assert (1, 2, 3, 4, 5, 6, 7, 8, 9)[start:end:step] == expected


@pytest.mark.parametrize(['data', 'index', 'new_index_value', 'expected'], [
    ([1, 2, 3, 4], 2, ('sdf', 'isn'), [1, 2, 'sdf', 'isn', 3, 4]),
    ([1, 2, 3, 4], 2, ['sdf', 'isn'], [1, 2, 'sdf', 'isn', 3, 4]),
    ([1, 2, 3, 4], 2, [('sdf', 'isn')], [1, 2, ('sdf', 'isn'), 3, 4]),
    ([1, 2, 3, 4], 0, [('sdf', 'isn')], [('sdf', 'isn'), 1, 2, 3, 4]),
])
def test_input_new_index(data, index, new_index_value, expected):
    data[index:index] = new_index_value
    assert data == expected
