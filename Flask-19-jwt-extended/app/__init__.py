from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_cors import CORS
from app.config import Config

db = SQLAlchemy()
jwt = JWTManager()
api = Api(default_mediatype="application/json")


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    jwt.init_app(app)
    from app import routes
    api.init_app(app)
    CORS(app)

    return app
