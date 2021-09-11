#!flask/bin/python
from flask import Flask

app = Flask("MyFlaskApp")


@app.route('/')
def hello_world():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)
