# Let's make our function func more usual. Let it take some argument arg.
# Return the argument value without any changes.
import pytest


def func(arg):
    return arg


@pytest.mark.parametrize("arg", [
    "awdac",
    2,
    3231,
    ["as", "sa", "sad"]
])
def test_func(arg):
    assert func(arg) == arg
