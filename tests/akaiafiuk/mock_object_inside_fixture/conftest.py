import pytest
from tests.akaiafiuk.mock_object_inside_fixture.device import Device


@pytest.fixture(scope="session", autouse=True)
def device():
    device = Device()
    return device


@pytest.fixture(autouse=True)
def health_check(device):
    device.validate_device()
