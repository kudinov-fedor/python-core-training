import pytest


@pytest.mark.parametrize(["par1", "res"], [
    (["a", 0, True, (1, 2, 3)], False),
    (["a", -1, True, (1, 2, 3)], True),
    (["a", -1, False, (1, 2, 3)], False),
    (["a", -1, True, ()], False)
])
def test_true_or_false(par1, res):
    result = all(par1)
    assert result is res


def test_filter_logic():
    data = ["cat", "dog", "", None, False, 0, 1, -2, True]
    text = list(filter(lambda i: isinstance(i, str) or isinstance(i, bool), data))
    assert type(int) not in text
