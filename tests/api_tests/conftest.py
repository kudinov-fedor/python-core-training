import os
import pytest

from api_testing.helpers.api_client import ApiClient


BOARD_NAME = "TEST_BOARD"
VAULT_NAME = "TEST_VAULT_BOARD"
LIST_NAME = "TEST_LIST"


@pytest.fixture(scope="session")
def samples_path():
    return os.path.join(os.path.dirname(__file__), "sample_data")


@pytest.fixture(scope="session")
def client():
    return ApiClient()


@pytest.fixture(scope="session", autouse=True)
def board_id(client: ApiClient):
    # reset board with name BOARD_NAME
    for board in client.get_boards():
        if board["name"] == BOARD_NAME:
            client.delete_board(board["id"])

    res = client.create_board(BOARD_NAME)
    return res["id"]


@pytest.fixture(scope="session", autouse=True)
def vault_id(client: ApiClient):
    # reset board with name VAULT_NAME
    for board in client.get_boards():
        if board["name"] == VAULT_NAME:
            client.delete_board(board["id"])

    res = client.create_board(VAULT_NAME)
    return res["id"]


@pytest.fixture(scope="function", autouse=True)
def flush_board(client, board_id, vault_id):
    # move all lists from BOARD_NAME board to VAULT_NAME board
    for _list in client.get_lists(board_id):
        client.move_list_to_board(_list["id"], vault_id)


@pytest.fixture()
def list_id(client: ApiClient, board_id, vault_id):
    # reset board with name BOARD_NAME
    list_id = client.create_list(name=LIST_NAME, board_id=board_id)
    return list_id["id"]


@pytest.fixture()
def card_id(client: ApiClient, list_id):
    # reset board with name BOARD_NAME
    card_id = client.create_card(name=LIST_NAME, list_id=list_id)
    return card_id["id"]
