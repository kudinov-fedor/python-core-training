import pytest


def test_player():
    assert True  # Pass


def test_length():
    a = '012345'
    res = len(a)
    assert res == 6  # Pass


def test_math_1():
    m = 10 * 5 - 40
    s = sum([1, 3, 6])
    total = sum([m, s])
    assert total == 20  # Pass


def test_amount():
    c = ['Cat', 'Dog', 'Bird', 'Cat', 'Pig', 'Cat']
    res_2 = c.count('Cat')
    assert res_2 == 3  # Pass


def test_format():
    f = format(666, 'b')
    assert f == '1010011010'  # It returns binary code as a string?


def test_bool():
    x = bool
    assert x != x  # Test Failed but expected and actual result are the same. Why?


def inc(x):
    return x + 1


def st(s):
    return s + ' is the best OS ever'


def test_answer1():
    assert inc(3) == 4  # Pass


def test_answer2():
    assert inc(29) == 31  # Fail, should be 30


def test_answer3():
    assert st('Windows') == 'Windows is the best OS ever'  # Pass


@pytest.fixture()
def fixture():
    return 'True'


def test_true(fixture):
    assert fixture == 'True'  # Pass


@pytest.mark.parametrize('number1', [0, 1, 2, 3, 5, 20, 150])
def test_pass(number1):
    assert number1 >= 0  # All pass


@pytest.mark.parametrize('number2', [0, 1, 2, 3, 5, 20, 150])
def test_fail(number2):
    assert number2 > 2  # 0, 1, 2 will fail, rest will pass


