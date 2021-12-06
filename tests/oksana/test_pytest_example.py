import pytest

@pytest.mark.smoke
def test_assert():
    assert 5 in [5,6,7]

@pytest.mark.parametrize("test_data, expected",[('test','testtesttest')])
def test_data(test_data, expected):
    assert test_data*3 == expected


