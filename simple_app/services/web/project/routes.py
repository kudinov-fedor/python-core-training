import os
import logging
from project import app, db

from werkzeug.utils import secure_filename
from flask import (
    Flask,
    jsonify,
    send_from_directory,
    request,
    redirect,
    url_for,
    render_template
)

from project.models import User

logger = logging.getLogger(__name__)


@app.route("/")
def main():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))
    users = User.query.paginate(page, per_page, error_out=False).items
    return render_template('main.html', users=users)


@app.route("/hello")
def hello_world():
    return jsonify(hello="world")


@app.route('/users', methods=['GET'])
def users():

    logger.info("hi info")
    logger.debug("hi debug")
    logger.warning("hi warning")
    logger.error("hi error")

    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))

    users = User.query.paginate(page, per_page, error_out=False)
    return jsonify(data=[i.as_dict() for i in users.items])


@app.route('/user/<int:_id>', methods=['GET'])
def user(_id: int):
    user = User.query.get_or_404(_id, description="User not found")
    return jsonify(data=user.as_dict())


@app.route("/factorial")
def factorial():
    print(request.args)
    n = int(request.args.get("n", 0))
    res = 1
    for i in range(1, n + 1):
        res *= i

    return jsonify(result=str(res))


@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)


@app.route("/media/<path:filename>")
def mediafiles(filename):
    return send_from_directory(app.config["MEDIA_FOLDER"], filename)


@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["MEDIA_FOLDER"], filename))
    return """
    <!doctype html>
    <title>upload new File</title>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file><input type=submit value=Upload>
    </form>
    """
