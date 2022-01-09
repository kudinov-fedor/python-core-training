from typing import List, Optional

from project.models import Book, Author


def publish_book(author_id: int, title: str) -> int:
    book = Book(author_id=author_id, title=title)
    book.add(book)
    book.commit()
    return book.book_id


def get_book(book_id: int) -> Book:
    return Book.query.filter(Book.book_id == book_id).one_or_none()


def search_by_title(title: str) -> List[Book]:
    return Book.query.filter(Book.title.like(f"%{title}%")).all()


def search_author(first_name: str, last_name: str) -> Optional[int]:
    author = Author.query(Author.author_id).filter(
        Author.first_name == first_name,
        Author.last_name == last_name,
    ).one_or_none()
    if author:
        return author.author_id


def add_author(first_name: str, last_name: str) -> int:
    author = Author(first_name=first_name, last_name=last_name)
    author.add().commit()
    return author.author_id


def publish_new_book(
    title: str, author_name: str, author_last_name: str):
    author_id = search_author(author_name, author_last_name)
    if author_id is None:
        author_id = add_author(author_name, author_last_name)
    publish_book(author_id, title)
