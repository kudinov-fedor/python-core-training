from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


from project.models import *  # noqa: E402, F403
from project.routes import *  # noqa: E402, F403
