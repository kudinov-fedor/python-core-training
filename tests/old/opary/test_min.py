import pytest


def test_min_true1():
    a = [59, 745, 9, -3, 91]
    res = min(a)
    assert res == -3


def test_min_true2():
    b = [12, 71, 0, 51, 264]
    res = min(b)
    assert res == 0


def test_min_true3():
    c = [93, 4325, -135, 71, 39]
    res = min(c)
    assert res == -135


def test_min_true4():
    float_nmbrs_list = ['7.91', '5.15', '79.35']
    res = min(float_nmbrs_list)
    assert res == '5.15'


def test_min_true5():
    list_of_str = ['banana', 'coffee', 'siebentausendzweihundertvierundfünfzig']
    res = min(list_of_str)
    print(res)
    assert res == 'banana'


@pytest.mark.parametrize('item, expected_min', [
    ([59, 745, 9, -3, 91], -3),
    ([12, 71, 0, 51, 264], 0),
    ([93, 4325, -135, 71, 39], -135),
    ([(10, "aB", 5), (10, "aC", 1), (10, "aa", 1)], (10, "aB", 5))
])
def test_min_parametrize(item, expected_min):
    a = item
    res = min(a)
    assert res == expected_min
