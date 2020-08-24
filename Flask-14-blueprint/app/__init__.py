from flask import Flask
from .views.index import index_blueprint
from . import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(index_blueprint)

    return app