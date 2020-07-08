from flask import Flask, render_template, request, flash

app = Flask(__name__)

# 导入tf扩展的表单类
from flask_wtf import FlaskForm

# 导 入自定义表单需要的字段
from wtforms import SubmitField, StringField, PasswordField

# 导入wtf扩展提供的表单验证
from wtforms.validators import DataRequired, EqualTo


# 自定义表单类、文本字段、密码字段、提交按钮
# 使用WTF实现表单 需要自定义一个表单类
class LoginForm(FlaskForm):
    # StringField/PasswordField是区别文本框类型， 用户名/密码是指定label值， validators 就是指明要验证哪些项
    username = StringField('用户名:', validators=[DataRequired()])
    password = PasswordField('密码:', validators=[DataRequired()])
    password2 = PasswordField('确认密码:', validators=[DataRequired(), EqualTo('password', '密码填入的不一致')])
    submit = SubmitField('提交')


# 定义根路由视图函数，生成表单对象，获取表单数据，进行表单数据验证
@app.route('/form', methods=['GEt', 'POST'])
def login():
    # 由RegisterForm类生成一个表实例
    login_form = LoginForm()
    
    # 逻辑处理
    if request.method == 'POST':
        
        # 获取请求的参数
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        
        # 调用validation_on_submit方法，可以一次性执行完所有验证函数的逻辑
        if login_form.validate_on_submit():
            # 进入这里就表示所有的逻辑都验证成功
            print(username)
            return 'success'
        
        else:
            # message = register_form.get('password2')[0]
            # flash(message)
            flash('参数有误')
    
    # 把实例化后的register_form传入到页面wtf.html中
    return render_template('login.html', form=login_form)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__mian__':
    app.run()
