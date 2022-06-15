import pytest


@pytest.mark.parametrize("p1, p2, res", [
    (10, 5, 2), # for test1
    (-4, 2, -2), # for test2
    (20, 10, 2), # jjll
])
def test_division(p1, p2, res):
    assert p1 / p2 == res
    

@pytest.mark.smoke
@pytest.mark.skip("cause of skipping")
def test_error():
    res = 3 != 3
    print(res)
    assert res

