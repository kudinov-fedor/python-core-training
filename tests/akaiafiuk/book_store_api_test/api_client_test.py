from akaiafiuk.book_store_api import ApiClient
from random import randint


random_name = 'akaiafiuk' + str(randint(1, 100000))


def test_flow():
    # Step 1: Create new instance of ApiClient
    api_client = ApiClient(login=random_name)

    # Step 2: Create a new user. Verify that login is correct and verify the user is not authorized
    api_client.create_user()
    assert api_client.username == random_name
    assert not api_client.is_authorized()

    # Step 3: Generate a user token and login the user. Verify that user is authorized
    api_client.generate_token()
    api_client.log_in()
    assert api_client.is_authorized()

    # Step 4. Get user data and verify that it is correct
    user_data = api_client.get_user_data()
    assert user_data.get('userId') == api_client.userid
    assert user_data.get('username') == api_client.username
    assert user_data.get('books') == []

    # Step 5. Logout and verify that values were erased
    api_client.log_out()
    assert not api_client.userid
