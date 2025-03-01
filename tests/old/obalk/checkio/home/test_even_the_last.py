import pytest

from obalk.checkio.home.even_the_last import even_the_last


@pytest.mark.parametrize("numbers, result", [
    ([], 0),
    ([43, 91, -86, 64, 25, -85, -71, -73, 23, 89, 10, 21, -78], 10452),
    ([69, -91, -49, -29, 13, -42, 34, -99, -97, -80, 16, -9], 126),
    ([69, -91, 0], 0)

])
def test_even_the_last(numbers, result):
    assert even_the_last(numbers) == result
