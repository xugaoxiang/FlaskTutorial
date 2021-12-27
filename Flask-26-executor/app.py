from flask import Flask
from flask_executor import Executor

app = Flask(__name__)

executor = Executor(app)


def send_email(recipient, subject, body):
    # 模拟邮件发送动作
    print('send mail.')
    return True


def callback(future):
    print('callback')


@app.route('/signup')
def signup():
    executor.add_default_done_callback(callback)
    executor.submit(send_email, "test@gmail.com", "subject", "body")
    return "signup done."


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=5000)
