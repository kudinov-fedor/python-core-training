import pytest

from tests.demoqa.books_app.api_client import ApiClient
from tests.demoqa.books_app.constants import USER, PASSWORD


@pytest.fixture(scope="session")
def user():
    user = ApiClient(USER, PASSWORD)
    user.create()
    yield user
    user.reset()


@pytest.fixture(autouse=True)
def remove_books(user):
    user.books_delete()


def test_add_books(user: ApiClient):
    books = user.books_get()["books"]
    assert len(books) == 8

    assert len(user.user_get()["books"]) == 0
    user.books_add(books[0]["isbn"])
    assert len(user.user_get()["books"]) == 1
    user.books_add(books[1]["isbn"])
    assert len(user.user_get()["books"]) == 2


def test_add_books_2(user: ApiClient):
    books = user.books_get()["books"]
    assert len(books) == 8

    assert len(user.user_get()["books"]) == 0
    user.books_add(books[0]["isbn"],
                   books[1]["isbn"])
    assert len(user.user_get()["books"]) == 2


def test_remove_book(user: ApiClient):
    books = user.books_get()["books"]
    assert len(books) == 8

    assert len(user.user_get()["books"]) == 0
    user.books_add(books[0]["isbn"])
    assert len(user.user_get()["books"]) == 1
    user.book_delete(books[0]["isbn"])
    assert len(user.user_get()["books"]) == 0
