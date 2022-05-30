import pytest


def test_sample_ayefi():
    assert 1 == 1

def test_pass():
    pass

@pytest.mark.skip("because it is awful")
def test_error():
    res = 1 != 1
    print(res)
    assert res

@pytest.mark.parametrize("param1, param2, res", [
    (5, 2, 2.5),
    (-4, 2, -2),
    (0, 4 , 0),
])
def test_division(param1, param2, res):
    assert param1 / param2 == res

#Home task
@pytest.mark.parametrize('data, res', [
    ('some', 4),
    ('change', 6),
    ('123', 3)
])
def test_len(data, res):
    assert len(data) == res

@pytest.fixture()
def test_list():
    return [1, 2, 3]
def test_append(test_list):
    test_list.append(4)
    assert test_list == [1, 2, 3, 4]