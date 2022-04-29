import pytest
from akaiafiuk.book_store_api import ApiClient


@pytest.fixture
def user():
    api_client = ApiClient()
    if api_client.user_exists():
        api_client.delete_user()
    api_client.create_user()
    yield api_client
    if api_client.user_exists():
        api_client.delete_user()
