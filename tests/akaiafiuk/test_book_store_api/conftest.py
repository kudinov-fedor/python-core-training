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


@pytest.fixture(scope='session')
def api_client():
    return ApiClient()


@pytest.fixture(scope='session')
def books(api_client):
    return api_client.get_all_books()
