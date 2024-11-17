# flask --app flask_app run


from flask import Flask, request

app = Flask(__name__)


# in memory db
BOOKS_DB = [{"book_id": 1, "book_name": "Hi there"},
            {"book_id": 2, "book_name": "How are you?"}]


@app.route('/book', methods=['GET'])
def show_books():
    count = request.args.get('count')
    count = int(count) if count else None
    return {"books": BOOKS_DB[:count]}


@app.route('/book/<int:book_id>', methods=['GET'])
def show_book(book_id):
    return {book["book_id"]: book for book in BOOKS_DB}[book_id]


@app.route('/book', methods=['POST'])
def create_book():
    data = request.get_json()
    data["book_id"] = int(len(BOOKS_DB))
    BOOKS_DB.append(data)
    return data
