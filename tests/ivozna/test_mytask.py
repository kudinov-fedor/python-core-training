from ivozna.my_task import mult_two


def test_mytask():
    res = mult_two(2, 6)
    assert res == 12
