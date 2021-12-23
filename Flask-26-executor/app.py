from flask import Flask
from flask_executor import Executor

app = Flask(__name__)

executor = Executor(app)


def send_email(recipient, subject, body):
    # Magic to send an email
    return True


@app.route('/signup')
def signup():
    # Do signup form
    executor.submit(send_email, recipient, subject, body)
