from sanic import Sanic
from sanic.response import text

app = Sanic("MySanicApp")


@app.get("/")
async def hello_world(request):
    return text("Hello, world.")


if __name__ == '__main__':
    app.run(debug=True)
