import pytest

from akaiafiuk.book_store_api import ApiClient
from random import randint


random_name = 'akaiafiuk' + str(randint(1, 100000))


@pytest.fixture
def user():
    api_client = ApiClient(login=random_name)
    api_client.create_user()
    yield api_client
    if api_client.user_id is not None and api_client.token is not None:
        api_client.delete_user()


def test_flow(user):

    # Step 1: Verify that login is correct and verify the user is not authorized
    assert user.username == random_name
    assert not user.is_authorized()

    # Step 2: Generate a user token and login the user. Verify that user is authorized
    user.prepare_user()
    assert user.is_authorized()

    # Step 4. Get user data and verify that it is correct
    user_data = user.get_user_data()
    assert user_data['userId'] == user.userid
    assert user_data['username'] == user.username
    assert user_data['books'] == []

    # Step 5. Logout and verify that values were erased
    user.log_out()
    assert not user.userid
