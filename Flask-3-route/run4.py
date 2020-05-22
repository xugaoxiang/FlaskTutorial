from flask import Flask


app = Flask(__name__)


def index():
    return 'Hello flask!'

app.add_url_rule('/', "index", index)


if __name__ == '__main__':
    app.run(debug=True)