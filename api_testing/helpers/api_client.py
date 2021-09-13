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
        res = self.client.get(self.host + "/1/members/me/boards")
        res.raise_for_status()
        return res.json()

    def get_board(self, board_id):
        url = "/1/boards/{}".format(board_id)
        res = self.client.get(self.host + url)
        res.raise_for_status()
        return res.json()

    def create_board(self, name):
        res = self.client.post(self.host + "/1/boards", json={"name": name})
        res.raise_for_status()
        return res.json()

    def delete_board(self, board_id):
        res = self.client.delete(self.host + "/1/boards/{}".format(board_id))
        res.raise_for_status()
        return res.json()

    def get_lists(self, board_id):
        res = self.client.get(self.host + "/1/boards/{}/lists".format(board_id))
        res.raise_for_status()
        return res.json()

    def create_list(self, *, name, board_id):
        res = self.client.post(self.host + "/1/lists".format(board_id),
                               json={"idBoard": board_id, "name": name})
        res.raise_for_status()
        return res.json()

    def archive_list(self, list_id):
        res = self.client.put(self.host + "/1/lists/{}/closed".format(list_id), params={"value": True})
        res.raise_for_status()
        return res.json()

    def unarchive_list(self, list_id):
        res = self.client.put(self.host + "/1/lists/{}/closed".format(list_id), params={"value": False})
        res.raise_for_status()
        return res.json()

    def move_list_to_board(self, list_id, board_id):
        res = self.client.put(self.host + "/1/lists/{}/idBoard".format(list_id), params={"value": board_id})
        res.raise_for_status()
        return res.json()

    def get_cards(self, board_id):
        res = self.client.get(self.host + "/1/boards/{}/cards".format(board_id))
        res.raise_for_status()
        return res.json()

    def get_card(self, card_id):
        res = self.client.get(self.host + "/1/cards/{}".format(card_id))
        res.raise_for_status()
        return res.json()

    def create_card(self, *, name, list_id):
        res = self.client.post(self.host + "/1/cards", json={"name": name, "idList": list_id})
        res.raise_for_status()
        return res.json()

    def delete_card(self, card_id):
        res = self.client.delete(self.host + "/1/cards/{}".format(card_id))
        res.raise_for_status()
        return res.json()

    def get_board_by_card(self, card_id):
        res = self.client.get(self.host + "/1/cards/{}/board".format(card_id))
        res.raise_for_status()
        return res.json()

    def get_list_by_card(self, card_id):
        res = self.client.get(self.host + "/1/cards/{}/list".format(card_id))
        res.raise_for_status()
        return res.json()

    def create_attachment(self, card_id, *, path, name=None, set_cover=True):

        name = name or path.split("/")[-1]
        res = self.client.post(self.host + "/1/cards/{}/attachments".format(card_id),
                               data={"name": name, "setCover": set_cover},
                               files={"file": open(path, "rb")})
        res.raise_for_status()
        return res.json()

    def get_attachments(self, card_id):
        res = self.client.post(self.host + "/1/cards/{}/attachments".format(card_id))
        res.raise_for_status()
        return res.json()

    def download_attachment(self, url: str, path):
        path = path or url.split("/")[-1]
        res = self.client.get(url)
        res.raise_for_status()
        open(path, 'wb').write(res.content)
