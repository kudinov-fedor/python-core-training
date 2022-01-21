import logging.config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


logging.basicConfig(level=logging.DEBUG,
                    format="MAIN %(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s")

# logging.config.fileConfig('logging.cfg', disable_existing_loggers=False)  # use logging config


from project.models import *  # noqa: E402, F403
from project.routes import *  # noqa: E402, F403
