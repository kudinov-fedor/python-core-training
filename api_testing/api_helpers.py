import os

from requests import session


class ApiClient:

    host = "https://api.trello.com"

    def __init__(self):

        api_key = os.environ["API_KEY"]
        api_token = os.environ["API_TOKEN"]

        self.client = session()
        self.client.headers = {
            "Authorization": 'OAuth oauth_consumer_key = "{}", oauth_token = "{}"'.format(api_key, api_token)}

    def get_boards(self):
        url = "/1/members/me/boards"
        res = self.client.get(self.host + url)
        res.raise_for_status()
        return res.json()

    def get_board(self, board_id):
        url = "/1/boards/{}".format(board_id)
        res = self.client.get(self.host + url)
        res.raise_for_status()
        return res.json()

    def get_lists(self, board_id):
        res = self.client.get(self.host + "/1/boards/{}/lists".format(board_id))
        res.raise_for_status()
        return res.json()

    def get_cards(self, board_id):
        res = self.client.get(self.host + "/1/boards/{}/cards".format(board_id))
        res.raise_for_status()
        return res.json()

    def get_card(self, card_id):
        res = self.client.get(self.host + "/1//cards/{}".format(card_id))
        res.raise_for_status()
        return res.json()

    def get_board_by_card(self, card_id):
        res = self.client.get(self.host + "/1//cards/{}/board".format(card_id))
        res.raise_for_status()
        return res.json()

    def get_list_by_card(self, card_id):
        res = self.client.get(self.host + "/1//cards/{}/list".format(card_id))
        res.raise_for_status()
        return res.json()
