import pytest


@pytest.mark.parametrize("inst, cls", [
    ('4.4', str),
    (3, int),
    (False, bool),
])
def test_is_instance(inst, cls):
    assert True == isinstance(inst, cls)


@pytest.mark.parametrize("seq, reverse", [
    ('qwe', ['e', 'w', 'q']),
    ([1, 2, 3], [3, 2, 1]),
])
def test_reversed(seq, reverse):
    assert list(reversed(seq)) == reverse


@pytest.mark.parametrize("digs, result", [
    ((3, 1, 5), 9),
    ([2, 2, 2.3], 6.3),
])
def test_sum(digs, result):
    assert sum(digs) == result