from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Table

from project import db


class User(db.Model):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String(128), unique=True, nullable=False)
    active = Column(Boolean(), default=True, nullable=False)

    books = relationship("Book", secondary=Table('user_to_book', db.Model.metadata,
                                                 Column('user_id', ForeignKey('user.id')),
                                                 Column('book_id', ForeignKey('book.id'))))  # many-to-many

    def __init__(self, email, books=None):
        self.email = email
        self.books = books or []

    def as_dict(self):
        return {'id': self.id,
                'email': self.email,
                'active': self.active,
                'books': [b.as_dict() for b in self.books or []]}


class Book(db.Model):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey("author.id"), nullable=False)

    author = relationship("Author", back_populates="books")  # many to one

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def as_dict(self):
        return {'id': self.id,
                'title': self.title,
                'author': self.author.as_dict()}


class Author(db.Model):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    books = relationship("Book")  # one to many

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def as_dict(self):
        return {'id': self.id,
                'first_name': self.first_name,
                'last_name': self.last_name}
