from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required
from app.models import User
from app import jwt


@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        'code': 201,
        'message': "token expired"
    })


class Login(Resource):
    def __init__(self, **kwargs):
        self.logger = kwargs.get('logger')

    def post(self):
        code = None
        message = None
        token = None
        userid = None

        args = reqparse.RequestParser() \
            .add_argument('username', type=str, location='json', required=True, help="用户名不能为空") \
            .add_argument("password", type=str, location='json', required=True, help="密码不能为空") \
            .parse_args()

        flag_user_exist, flag_password_correct, user = User.authenticate(args['username'], args['password'])
        if not flag_user_exist:
            code = 201
            message = "user not exist"
        elif not flag_password_correct:
            code = 202
            message = "wrong password"
        else:
            code = 200
            message = "success"
            token = create_access_token(identity=user.username)
            userid = user.id

        return jsonify({
            "code": code,
            "message": message,
            "token": token,
            "userid": userid
        })


class Users(Resource):
    def __init__(self, **kwargs):
        self.logger = kwargs.get('logger')

    @jwt_required
    def get(self):
        users_list = []
        users = User.get_users()

        for user in users:
            users_list.append({"userid": user.id, "username": user.username})

        return jsonify({
            "code": 200,
            "message": "success",
            "users": users_list
        })
