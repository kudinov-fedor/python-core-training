# install:     pip install "fastapi[standard]"
# run command: fastapi dev fastapi_app.py
# host, port:  http://127.0.0.1:8000


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# in memory db
BOOKS_DB = [{"book_id": 0, "book_name": "Hi there"},
            {"book_id": 1, "book_name": "How are you?"}]


class Book(BaseModel):
    book_id: int | None = None
    book_name: str


@app.get("/book")
def read_root(count: int | None = None):
    return {"books": BOOKS_DB[:count]}


@app.get("/book/{book_id}")
def read_item(book_id: int):
    return {book["book_id"]: book for book in BOOKS_DB}[book_id]


@app.post("/book")
def update_item(book: Book):
    data = book.dict()
    data["book_id"] = int(len(BOOKS_DB))
    BOOKS_DB.append(data)
    return data
