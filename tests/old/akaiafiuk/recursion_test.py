import pytest
from akaiafiuk.recursion import unpack_while, unpack_recursion, unpack_recursion_state_transition


@pytest.mark.parametrize("func", [
    unpack_while,
    unpack_recursion,
    unpack_recursion_state_transition
])
def test_recursion(func):
    assert func(10) == [10]
    assert func([1, 2, 3]) == [1, 2, 3]
    assert func([1, [2, 3]]) == [1, 2, 3]
    assert func([1, [2, [3]]]) == [1, 2, 3]
    assert func([[[[1, 2, 3]]]]) == [1, 2, 3]
