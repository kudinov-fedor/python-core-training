# install:     pip install sanic
# run command: sanic sanic_app
# host, port:  http://127.0.0.1:8000


from sanic import Sanic, json

app = Sanic(__name__)


# in memory db
BOOKS_DB = [{"book_id": 0, "book_name": "Hi there"},
            {"book_id": 1, "book_name": "How are you?"}]


@app.route("/book")
async def show_books(request):
    count = request.args.get("count")
    count = int(count) if count else None
    return json({"books": BOOKS_DB[:count]})


@app.route('/book/<book_id:int>', methods=["GET"])
async def show_book(request, book_id):
    return json({book["book_id"]: book for book in BOOKS_DB}[book_id])


@app.post('/book')
async def create_book(request):
    data = request.json
    data["book_id"] = int(len(BOOKS_DB))
    BOOKS_DB.append(data)
    return json(data)
