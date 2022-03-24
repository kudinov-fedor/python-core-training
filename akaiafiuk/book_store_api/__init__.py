import requests
from requests import session
from akaiafiuk.book_store_api.constants import BASE_URL, USER, PASSWORD


class ApiClient:

    host = BASE_URL

    def __init__(self, login=USER, password=PASSWORD):
        self.login = login
        self.password = password
        self.user_id = None
        self.client = session()

    @property
    def token(self):
        return self.client.headers['Authorization']

    def create_user(self) -> dict:
        """
        Creates a new user
        :return: a dictionary with "userID"; "username", "books" keys
        """
        res = requests.post(self.host + '/Account/v1/user', data={
            "userName": self.login,
            "password": self.password
        })
        res.raise_for_status()
        return res.json()

    def is_authorized(self) -> bool:
        """
        Returns a bool flag is the user authorized
        :return: True or False
        """
        res = requests.post(self.host + '/Account/v1/Authorized', data={
            "userName": self.login,
            "password": self.password
        })
        res.raise_for_status()
        return res.text == 'true'

    def generate_token(self) -> str:
        """
        Generates a user token for a user
        :return: authorization token
        """
        res = requests.post(self.host + '/Account/v1/GenerateToken', data={
            "userName": self.login,
            "password": self.password
        })
        res.raise_for_status()
        return res.json().get("token")

    def log_in(self) -> str:
        """
        Sets a user id parameter to a User id of logged in user
        :return: user id
        """
        res = requests.post(self.host + '/Account/v1/Login', data={
            "userName": self.login,
            "password": self.password
        })
        res.raise_for_status()
        return res.json().get("userId")

    def prepare_user(self) -> None:
        """
        Generates and sets authorization token and user id
        :return:
        """
        self.client.headers.update({'Authorization': 'Bearer ' + self.generate_token()})
        self.user_id = self.log_in()

    def delete_user(self) -> None:
        """
        Deletes a user with the given credentials
        :return: None
        """
        res = self.client.delete(self.host + '/Account/v1/user/' + self.user_id)
        res.raise_for_status()

    def get_user_data(self) -> dict:
        """
        Returns user data for authorized user
        :return: a dictionary with keys "userID" -> str; "username" -> str, "books" -> list
        """
        res = self.client.get(self.host + '/Account/v1/user/' + self.user_id)
        res.raise_for_status()
        return res.json()

    def log_out(self) -> None:
        """
        Resets user id and authorization token
        :return: None
        """
        self.user_id = None
        del self.client.headers['Authorization']
