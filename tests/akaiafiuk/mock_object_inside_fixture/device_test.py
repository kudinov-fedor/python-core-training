import pytest


@pytest.mark.xfail("Expect this test to Fail, because of mock_device_class fixture")
def test_device():
    assert True
