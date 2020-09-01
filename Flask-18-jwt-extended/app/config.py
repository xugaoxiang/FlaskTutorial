import os


class Config:
    # flask
    DEBUG = os.environ.get('FLASK_DEBUG') or True

    # database
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'mysql+pymysql://root:toor@localhost/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # jwt
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-key'
    JWT_COOKIE_CSRF_PROTECT = True
    JWT_CSRF_CHECK_FORM = True
    JWT_ACCESS_TOKEN_EXPIRES = os.environ.get('JWT_ACCESS_TOKEN_EXPIRES') or 3600
    PROPAGATE_EXCEPTIONS = True
