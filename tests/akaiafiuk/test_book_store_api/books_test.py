import time

import pytest


def test_all_books(api_client):
    """Verify all books response format is correct and len is more than 0"""
    books = api_client.get_all_books()
    assert books
    isinstance(books, list)
    isinstance(books[0], dict)


def test_add_book_to_collection(user, books):
    """Verify adding a book into collection"""
    user.prepare_user()
    response = user.add_book_to_collection([books[0]['isbn']])
    assert response['books'][0]['isbn'] == books[0]['isbn']


def test_add_books_to_collection(user, books):
    """Verify adding multiple books into collection"""
    user.prepare_user()
    response = user.add_book_to_collection([books[0]['isbn'], books[1]['isbn']])
    assert response['books'][0]['isbn'] == books[0]['isbn']
    assert response['books'][1]['isbn'] == books[1]['isbn']


def test_replace_book_in_collection(user, books):
    """Replace one book to another inside a user's collection"""
    user.prepare_user()
    user.add_book_to_collection(books[0]['isbn'])
    response = user.replace_book_in_collection(books[0]['isbn'], books[1]['isbn'])
    assert response['books'][0]['isbn'] == books[1]['isbn']


def test_delete_book(user, books):
    """Delete a book from a user collection"""
    user.prepare_user()
    user.add_book_to_collection(books[0]['isbn'])
    assert books[0] in user.get_user_data()['books']
    user.delete_book_from_collection(books[0]['isbn'])
    assert books[0] not in user.get_user_data()['books']


@pytest.mark.skip(reason="This test fails because all books are removed from user's profile. Tools QA bug.")
def test_delete_books(user, books):
    """Delete multiple books from user's collection"""
    user.prepare_user()
    user.add_book_to_collection([books[0]['isbn'], [books[1]['isbn']], [books[2]['isbn']]])
    user_books = user.get_user_data()['books']
    assert books[0] in user_books
    assert books[1] in user_books
    user.delete_books_from_collection([books[0]['isbn'], books[1]['isbn']])
    user_books1 = user.get_user_data()['books']
    assert len(user_books1) == 1
    assert books[2] in user_books1
