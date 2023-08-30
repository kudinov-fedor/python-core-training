import pytest
import even_the_last


@pytest.mark.parametrize(["param", "res"], [
    ([-89, -86, 13, -69, 94, -75, 66, 97, -50], -1700),
    ([-78, -16, 84, 72, 33, -3, -9, -90, 13, -64, 10, -47, 99, -27, -87, -18, 76, -63], -8883),
    ([-40, 51, -71, -12, 24, -95, 20, 8, 68, -87, 28, 89, -1, 61, 40, 56, 16, 0], 0),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24], 0),
    ([-5, 94, 5, -28, 17, -72, 84, 85, -17, -96, -84, -76, 0, 75], 0),
    ([-94, 21, -58, 38, 56, 6, -91, -69, 39], -5772),
    ([28, 54, -7, 90, 64], 5440),
    ([39], 1521),
    ([-37, -36, -19, -99, 29, 20, 3, -7, -64, 84, 36, 62, 26, -76, 55, -24, 84, 49, -65, 41], 1968),
    ([43, 91, -86, 64, 25, -85, -71, -73, 23, 89, 10, 21, -78], 10452),
    ([-36, 82, -14, 82, -59, -35, -39, 33, 28, 27, -24, 6, 83, 39, 85, 58, -44, -18, -90, -75], 8250),
    ([69, -91, -49, -29, 13, -42, 34, -99, -97, -80, 16, -9], 126),
    ([-43, -72, 3, -83, -82, 93, -59, -80, 6, -39, 16, 39, 1, 47, -19, 67, 51], -6426),
    ([-80, -32, 52, -53, -21, -57, -58, -24, -15, -14, 97, -79, -35, 69], -4140),
    ([-77, -87, -10, 98, -65, -75, -26, -46, -54, 70, -52, -81, -94, 46], -17388),
    ([-88, 53, 55, -74, -36, 20, 95, -22, -63, -53, -68], 7140),
    ([45], 2025),
    ([72, -19, -73, -59, 83, -79, -90], 720)
])
def test_even_the_last(param, res):
    result = even_the_last.checkio(param)
    assert result == res