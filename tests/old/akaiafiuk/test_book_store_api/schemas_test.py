from cerberus import Validator

from tests.akaiafiuk.test_book_store_api.schemas import book, user_data


def test_books_item_schema(books):
    """Verify that schema for book data is correct"""
    assert Validator(book).validate(books[0])


def test_user_data_schema(prepared_user):
    """Verify that schema for user data is correct"""
    assert Validator(user_data).validate(prepared_user.get_user_data())
