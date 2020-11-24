from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def index():
    req = requests.get('http://127.0.0.1:5000/proxy')
    return req.text


@app.route('/proxy')
def proxy():
    return "Hello Flask."


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
