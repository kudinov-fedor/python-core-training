import requests


BASE_URL = 'https://demoqa.com'
USER_ID = '04f0b737-84b0-404a-9843-e2de337d371c'
USERNAME = 'akaiafiuk_3'
PASSWORD = 'H@ppy2code123'
NEW_USER = 'akaiafiuk_4'
ISBN = '9781449325862'
ISBN_REPLACE_TO = '9781449331818'


def is_authorized(username: str, password: str) -> bool:
    """
    Returns a bool flag is the user authorized
    :param username: Username
    :param password: Password
    :return: True or False
    """
    r = requests.post(BASE_URL + '/Account/v1/Authorized', data={
        "userName": username,
        "password": password
    })
    return bool(r.text)


def generate_token(username: str, password: str) -> str:
    """
    Return an authorization token
    :param username: Username
    :param password: Password
    :return: authorization token
    """
    r = requests.post(BASE_URL + '/Account/v1/GenerateToken', data={
        "userName": username,
        "password": password
    })
    return r.json().get("token")


def create_user(username: str, password: str) -> dict:
    """
    Creates a new user
    :param username: Username for the new user
    :param password: Password for the new user
    :return: a dictionary with "userID"; "username", "books" keys
    """
    r = requests.post(BASE_URL + '/Account/v1/user', data={
        "userName": username,
        "password": password
    })
    return r.json()


def delete_user(username: str, password: str, user_id) -> None:
    """
    Deletes a user with the given credentials
    :param username: Username of a user to remove
    :param password: Password of a user to remove
    :param user_id: User ID of a user to remove
    :return:
    """
    token = generate_token(username, password)
    requests.delete(BASE_URL + '/Account/v1/user/' + user_id, auth=token)


def get_user_data(username: str, password: str, user_id: str) -> dict:
    """
    Returns user data for authorized user
    :param username: Username
    :param password: Password
    :param user_id: User ID
    :return: a dictionary with keys "userID" -> str; "username" -> str, "books" -> list
    """
    token = generate_token(username, password)
    print(type(token))
    print(token)
    r = requests.get(BASE_URL + '/Account/v1/user/' + user_id, headers={'Authorization': 'Bearer ' + token})
    return r.json()
