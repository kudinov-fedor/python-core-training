"""
Create decorator which would remember answers,
and if answer was given, do not make a call to a function
"""
from decorator1_call_counter import my_decor


def test_counted():
    call_count = 0

    def original_func(n):
        nonlocal call_count
        call_count += 1
        return n

    wrapper = my_decor(original_func)
    wrapper(0)
    wrapper(1)
    wrapper(1)
    wrapper(2)
    wrapper(3)
    wrapper(2)
    wrapper(4)
    assert call_count == 5
    assert call_count
    assert callable(wrapper) is True
