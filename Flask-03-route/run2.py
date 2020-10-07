from flask import Flask

app = Flask(__name__)


@app.route('/home/<name>')
def index(name):
    return f"Welcome to home!{name}"


if __name__ == '__main__':
    app.run(debug=True)