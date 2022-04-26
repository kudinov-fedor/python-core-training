from requests import session
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
        self.client.headers.headers['Authorization'] = 'Bearer ' + value

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
