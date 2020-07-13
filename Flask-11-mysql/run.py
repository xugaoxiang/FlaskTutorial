from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length, Email
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "xxx"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///member.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)

class Member(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(45))
    email = db.Column(db.String(45))
    password = db.Column(db.String(128))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

db.create_all()


# 使用WTF实现表单，自定义一个表单类
class RegisterForm(FlaskForm):
    username = StringField(label='用户名: ', validators=[DataRequired()])
    email = StringField(label='邮箱: ', validators=[DataRequired(), Email(message='邮箱格式错误')])
    password = PasswordField(label='密码: ', validators=[DataRequired(), Length(6, 16, message='密码格式错误')])
    password2 = PasswordField(label='确认密码: ', validators=[DataRequired(), Length(6, 16, message='密码格式错误'),
                                                          EqualTo('password', message='密码不一致')])
    submit = SubmitField(label='注册')


@app.route('/', methods=['GEt', 'POST'])
def register():
    register_form = RegisterForm()

    if request.method == 'POST':
        if register_form.validate_on_submit():
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')
            password2 = request.form.get('password2')

            member = Member(username=username, email=email, password=password)
            db.session.add(member)
            db.session.commit()

        else:
            return 'Invalid'

    # 把实例化后的register_form传入到页面register.html中
    return render_template('register.html', form=register_form)


if __name__ == '__main__':
    app.run(debug=True)
