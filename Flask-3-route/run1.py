from flask import Flask

app = Flask(__name__)


@app.route('/home')
def index():
    return "Welcome to home!"


if __name__ == '__main__':
    app.run(debug=True)