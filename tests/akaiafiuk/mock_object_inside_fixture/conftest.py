import pytest
from tests.akaiafiuk.mock_object_inside_fixture.device import Device


@pytest.fixture(scope="session", autouse=True)
def device():
    device = Device()
    return device


@pytest.fixture(autouse=True)
def mock_device_class(mocker):
    mocker.patch.object(Device, 'get_version', return_value=None)


@pytest.fixture(autouse=True)
def health_check(device, mock_device_class):
    device.validate_device()
