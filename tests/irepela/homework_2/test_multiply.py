from irepela.homework_2.multiply import mult_two


def test_multiply():
    assert mult_two(3, 4) == 12
    assert mult_two(3, 2) == 6
    assert mult_two(0, 1) == 0
