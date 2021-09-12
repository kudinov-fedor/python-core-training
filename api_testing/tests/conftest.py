import pytest

from api_testing.helpers import helpers
from api_testing.helpers.constants import BOARD_NAME
from api_testing.helpers.api_client import ApiClient


@pytest.fixture(scope="session", autouse=True)
def board_id():
    helpers.delete_board_if_exists(BOARD_NAME)
    return helpers.get_or_create_board(BOARD_NAME)


@pytest.fixture(scope="session")
def client():
    return ApiClient()
