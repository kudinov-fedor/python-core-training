from requests import session
from typing import Union
from akaiafiuk.book_store_api.constants import BASE_URL, USER, PASSWORD, RETRY_TIMES


def retry(number_of_tries):
    def decorator(func: callable):
        def wrapper(*args, **kwargs):
            for current_try in range(number_of_tries):
                try:
                    res = func(*args, **kwargs)
                    return res
                except Exception as e:
                    print(e)
                    if current_try == number_of_tries - 1:
                        raise
        return wrapper
    return decorator


class ApiClient:
    host = BASE_URL

    def __init__(self, login=USER, password=PASSWORD):
        self.login = login
        self.password = password
        self.user_id = None
        self.client = session()

    @property
    def token(self):
        return self.client.headers.get('Authorization')

    @token.setter
    def token(self, value: str):
        self.client.headers['Authorization'] = 'Bearer ' + value

    @token.deleter
    def token(self):
        del self.client.headers['Authorization']

    def user_exists(self) -> bool:
        """
        Verifies if a user exists
        :return: True if exists, False if does not exist
        """
        return self.log_in() is not None

    def create_user(self) -> dict:
        """
        Creates a new user
        :return: a dictionary with "userID"; "username", "books" keys
        """
        res = self.client.post(self.host + '/Account/v1/user', data={
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
        res = self.client.post(self.host + '/Account/v1/Authorized', data={
            "userName": self.login,
            "password": self.password
        })
        res.raise_for_status()
        return res.text == 'true'

    def is_logged_in(self) -> bool:
        """
        Returns a bool flag if a user logged in
        :return: True or False
        """
        return self.log_in() is not None

    @retry(RETRY_TIMES)
    def generate_token(self) -> str:
        """
        Generates a user token for a user
        :return: authorization token
        """
        res = self.client.post(self.host + '/Account/v1/GenerateToken', data={
            "userName": self.login,
            "password": self.password
        })
        res.raise_for_status()
        if res.json()['token'] is None:
            raise RuntimeError("Failed to retrieve token")
        return res.json()["token"]

    def log_in(self) -> str or None:
        """
        Returns a string with user id if user exists or None
        :return: user id or None
        """
        user_id = None
        res = self.client.post(self.host + '/Account/v1/Login', data={
            "userName": self.login,
            "password": self.password
        })
        res.raise_for_status()
        if res.headers.get("Content-Type") is not None:
            user_id = res.json()["userId"]
        return user_id

    def prepare_user(self) -> None:
        """
        Generates and sets authorization token and user id
        :return:
        """
        self.token = self.generate_token()
        self.user_id = self.log_in()

    def delete_user(self) -> None:
        """
        Deletes a user with the given credentials
        :return: None
        """
        self.prepare_user()
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
        del self.token

    def get_all_books(self) -> list:
        """
        Returns a list with all available books
        :return: a list of dictionaries with available books and their info
        """
        res = self.client.get(self.host + '/BookStore/v1/Books')
        res.raise_for_status()
        return res.json()['books']

    def get_book_by_isbn(self, isbn: str) -> dict:
        """
        Returns a dictionary with the information about a given book
        :param isbn: isbn number of a book
        :return: a dictionary with book data
        """
        res = self.client.get(self.host + '/BookStore/v1/Book', params={'ISBN': isbn})
        res.raise_for_status()
        return res.json()

    def add_book_to_collection(self, isbn_numbers: Union[int, list]) -> dict:
        """
        Ads a book to a collection
        :param isbn_numbers: string or list of strings
        :return: dict with list of books available in user's collection
        """
        res = self.client.post(self.host + '/BookStore/v1/Books', json={
            "userId": self.user_id,
            "collectionOfIsbns": [{"isbn": isbn} for isbn in isbn_numbers] if isinstance(isbn_numbers, list)
            else [{"isbn": isbn_numbers}]
        })
        res.raise_for_status()
        return res.json()

    def replace_book_in_collection(self, isbn: str, isbn_replace_to: str) -> dict:
        """
        Replace one bok with another in a user collection
        :param isbn: str with isbn number of a user book
        :param isbn_replace_to: str with isbn of a book from a book store
        :return: a dict with user data
        """
        res = self.client.put(self.host + '/BookStore/v1/Books/' + isbn, json={
            "userId": self.user_id,
            "isbn": isbn_replace_to
        })
        res.raise_for_status()
        return res.json()

    def delete_book_from_collection(self, isbn: str) -> None:
        """
        Delete a book from a user collection
        :param isbn: isbn number of a book to delete
        :return: None
        """
        res = self.client.delete(self.host + '/BookStore/v1/Book', json={
            "isbn": isbn,
            "userId": self.user_id
        })
        res.raise_for_status()

    def delete_books_from_collection(self, isbn_numbers: Union[int, list]):
        res = self.client.delete(self.host + '/BookStore/v1/Books', params={
            "UserId": self.user_id
        }, json={
            "userId": self.user_id,
            "collectionOfIsbns": [{"isbn": isbn} for isbn in isbn_numbers] if isinstance(
                isbn_numbers, list)
            else [{"isbn": isbn_numbers}]
        })
        res.raise_for_status()
