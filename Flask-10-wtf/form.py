from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class UserRegisterForm(FlaskForm):
    username = StringField('用户名', [DataRequired('用户名必填！'), Length(min=6, max=20, message='用户名必须介于6-20字符！')])
    password = PasswordField('密码', [DataRequired('密码必填！'), Length(min=6, max=20, message='密码必须介于6-20字符！')])
    confirm = PasswordField('重复密码', [DataRequired('重复密码必填！'), EqualTo('password', message='两次密码输入不一致！')])
    email = StringField('邮箱', [DataRequired('邮箱必填！'), Email('邮箱格式不正确！')])