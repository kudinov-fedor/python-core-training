import requests
import os
from requests import session

BASE_URL = 'https://demoqa.com'
USER_ID = '04f0b737-84b0-404a-9843-e2de337d371c'
USER = 'akaiafiuk_3'
NEW_USER = 'akaiafiuk_4'
ISBN = '9781449325862'
ISBN_REPLACE_TO = '9781449331818'
PASSWORD = os.environ['PASSWORD']


class ApiClient:
    def __init__(self, login=USER, password=PASSWORD):
        self.login = login
        self.password = password
        self.user_id = None
        self.client = session()

    @property
    def username(self):
        return self.login

    @property
    def userid(self):
        return self.user_id

    def create_user(self) -> dict:
        """
        Creates a new user
        :return: a dictionary with "userID"; "username", "books" keys
        """
        res = requests.post(BASE_URL + '/Account/v1/user', data={
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
        res = requests.post(BASE_URL + '/Account/v1/Authorized', data={
            "userName": self.login,
            "password": self.password
        })
        res.raise_for_status()
        return res.text == 'true'

    def generate_token(self) -> None:
        """
        Generates a user token for a user
        :return: None
        """
        res = requests.post(BASE_URL + '/Account/v1/GenerateToken', data={
            "userName": self.login,
            "password": self.password
        })
        res.raise_for_status()
        self.client.headers.update({'Authorization': 'Bearer ' + res.json().get("token")})

    def log_in(self) -> None:
        """
        Sets a user id parameter to a User id of logged in user
        :return: None
        """
        res = requests.post(BASE_URL + '/Account/v1/Login', data={
            "userName": self.login,
            "password": self.password
        })
        res.raise_for_status()
        self.user_id = res.json().get("userId")

    def delete_user(self) -> None:
        """
        Deletes a user with the given credentials
        :return: None
        """
        res = self.client.delete(BASE_URL + '/Account/v1/user/' + self.user_id)
        res.raise_for_status()

    def get_user_data(self) -> dict:
        """
        Returns user data for authorized user
        :return: a dictionary with keys "userID" -> str; "username" -> str, "books" -> list
        """
        res = self.client.get(BASE_URL + '/Account/v1/user/' + self.user_id)
        res.raise_for_status()
        return res.json()

    def log_out(self) -> None:
        """
        Resets user id and authorization token
        :return: None
        """
        self.user_id = None
        self.client.headers.update({'Authorization': None})
