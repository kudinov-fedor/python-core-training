from dyurchen.multiply import mult_two


def test_multiply():
    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0