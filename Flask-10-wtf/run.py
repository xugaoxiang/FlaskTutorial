from flask import Flask, render_template, request

# 导入wtf扩展的表单类
from flask_wtf import FlaskForm

# 导入自定义表单需要的字段
from wtforms import SubmitField, StringField, PasswordField

# 导入wtf扩展提供的表单验证
from wtforms.validators import DataRequired, EqualTo, Length, Email

app = Flask(__name__)
app.secret_key = "xxx"


# 自定义表单类、文本字段、密码字段、提交按钮
# 使用WTF实现表单 需要自定义一个表单类
class RegisterForm(FlaskForm):
    # StringField/PasswordField是区别文本框类型， 用户名/密码是指定label值， validators 就是指明要验证哪些项
    username = StringField(label='用户名:', validators=[DataRequired()])
    email = StringField(label='邮箱:', validators=[DataRequired(), Email(message='邮箱格式错误')])
    password = PasswordField(label='密码:', validators=[DataRequired(), Length(6, 16, message='密码格式错误')])
    password2 = PasswordField(label='确认密码:', validators=[DataRequired(), Length(6, 16, message='密码格式错误'),
                                                         EqualTo('password', message='密码不一致')])
    submit = SubmitField(label='提交')


# 定义根路由视图函数，生成表单对象，获取表单数据，进行表单数据验证
@app.route('/', methods=['GEt', 'POST'])
def login():
    # 由RegisterForm类生成一个表实例
    register_form = RegisterForm()

    # 逻辑处理
    if request.method == 'POST':
        # 调用validation_on_submit方法，可以一次性执行完所有验证函数的逻辑
        if register_form.validate_on_submit():
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')
            password2 = request.form.get('password2')

            if username == 'xgx' and password == password2 and email == 'test@gmail.com':
                # 进入这里就表示所有的逻辑都验证成功
                return 'Register success, username: {}, email: {}, password: {}'.format(username, email, password)
            else:
                return 'Error'
        else:
            return 'Invalid'

    # 把实例化后的register_form传入到页面wtf.html中
    return render_template('register.html', form=register_form)


if __name__ == '__main__':
    app.run(debug=True)
