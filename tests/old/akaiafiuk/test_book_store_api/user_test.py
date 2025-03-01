import pytest
import requests

from datetime import datetime, timezone, timedelta
from old.akaiafiuk.book_store_api.constants import USER
from old.akaiafiuk.book_store_api import ApiClient


def test_verify_user_created(user):
    """
    Verify that login is correct and verify the user is not authorized
    """
    assert user.login == USER
    assert not user.is_authorized()


def test_verify_user_logged_in(user):
    """
    Generate a user token and login the user. Verify that user is authorized
    """
    user.prepare_user()
    assert user.is_authorized()


def test_verify_default_user_data(user):
    """
    Verify that user data is correct after user is created and logged in
    """
    user.prepare_user()
    user_data = user.get_user_data()
    assert user_data['userId'] == user.user_id
    assert user_data['username'] == user.login
    assert user_data['books'] == []


def test_verify_data_erased_after_logout(user):
    """
    Verify that User ID is erased after logout
    """
    user.prepare_user()
    user.log_out()
    assert not user.user_id


def test_login_using_invalid_credentials():
    """
    Verify that log_in method returns None for non existent user
    """
    api_client = ApiClient(login='non_existent', password='123')
    assert not api_client.user_exists()
    assert not api_client.is_logged_in()


def test_delete_user(user):
    """
    Verify that log_in method returns None for deleted user
    """
    user.delete_user()
    assert not user.user_exists()


def test_create_user_which_already_registered(user):
    """Verify that 406 error is raised in case when user already exists"""
    with pytest.raises(requests.exceptions.HTTPError, match=r"406 Client Error: Not Acceptable"):
        user.create_user()


def test_register_using_weak_password():
    """
    Verify that user is not created in case of weak password was used
    """
    api_client = ApiClient(password='123')
    with pytest.raises(requests.exceptions.HTTPError, match=r"400 Client Error: Bad Request"):
        api_client.create_user()


def test_token_expiration_date(user):
    """Verify that token expiration date is 7 days ahead of the current date"""
    expected_expiration = (datetime.now(timezone.utc) + timedelta(days=7)).strftime("%Y-%m-%d")
    assert expected_expiration in user.generate_token()['expires']
