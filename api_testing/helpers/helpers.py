from api_testing.helpers.api_client import ApiClient


def get_or_create_board(name):
    boards = {board["name"]: board["id"] for board in ApiClient().get_boards()}
    if name not in boards:
        res = ApiClient().create_board(name)
        board_id = res["id"]
    else:
        board_id = boards["name"]
    return board_id


def delete_board_if_exists(name):
    boards = {board["name"]: board["id"] for board in ApiClient().get_boards()}
    if name in boards:
        ApiClient().delete_board(boards[name])
