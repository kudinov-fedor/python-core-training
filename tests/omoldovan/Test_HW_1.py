import pytest
#
#
# def test_sample():
#     assert 1 == 1
#
#
# def test_sample_2():
#     pass
#
#
# def test_error():
#     res = 1 != 1
#     print(res)
#     assert res


@pytest.mark.parametrize('param1, param2, res', [
    [6, 2, 3],      # positive/positive --PASS
    [2, 1, 1],      # positive/positive --FAIL
    [24, -3, -8],   # positive/negative
    [0, 6, 0]       # zero division

])
def test_zero_dev_with_param(param1, param2, res):
    assert param1/param2 == res


@pytest.mark.skip("Just for fun")
def test_error():
    res = 1 != 1
    print(res)
    assert res