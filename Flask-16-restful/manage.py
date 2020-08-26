import logging.config
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "stream": "ext://sys.stdout",
            },
            "info_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "INFO",
                "formatter": "simple",
                "filename": "info.log",
                "maxBytes": 10485760,
                "backupCount": 50,
                "encoding": "utf8",
            },
            "error_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "ERROR",
                "formatter": "simple",
                "filename": "errors.log",
                "maxBytes": 10485760,
                "backupCount": 20,
                "encoding": "utf8",
            },
            "debug_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "filename": "debug.log",
                "maxBytes": 10485760,
                "backupCount": 50,
                "encoding": "utf8",
            },
        },
        "loggers": {
            "my_module": {"level": "ERROR", "handlers": ["console"], "propagate": "no"}
        },
        "root": {
            "level": "DEBUG",
            "handlers": ["error_file_handler", "debug_file_handler"],
        },
    }
)

USERS = [
    {"name": "zhangsan"},
    {"name": "lisi"},
    {"name": "wangwu"},
    {"name": "zhaoliu"}
]

class Users(Resource):
    def __init__(self, **kwargs):
        self.logger = kwargs.get('logger')

    def get(self):
        return jsonify(USERS)

    def post(self):
        args = reqparse.RequestParser() \
            .add_argument('name', type=str, location='json', required=True, help="名字不能为空") \
            .parse_args()

        self.logger.debug(args)

        if args['name'] not in USERS:
            USERS.append({"name": args['name']})

        return jsonify(USERS)

    def delete(self):
        USERS = []
        return jsonify(USERS)


class UserId(Resource):
    def __init__(self, **kwargs):
        self.logger = kwargs.get("logger")

    def get(self, userid):
        return jsonify(
            {"name": USERS[int(userid)].get("name")}
        )


app = Flask(__name__)
api = Api(app, default_mediatype="application/json")

api.add_resource(Users, '/users', resource_class_kwargs={
    "logger": logging.getLogger('/Users')
})

api.add_resource(UserId, '/user/<userid>', resource_class_kwargs={
    "logger": logging.getLogger('/UserId')
})

app.run(host='0.0.0.0', port=5001, use_reloader=True, debug=True)