from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

USERS = [
    {"name": "zhangsan"},
    {"name": "lisi"},
    {"name": "wangwu"},
    {"name": "zhaoliu"}
]

class Users(Resource):
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


app = Flask(__name__)
CORS(app)
api = Api(app, default_mediatype="application/json")

api.add_resource(Users, '/users')

app.run(host='0.0.0.0', port=5001, use_reloader=True, debug=True)