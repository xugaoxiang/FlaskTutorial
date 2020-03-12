from flask import Flask

# 创建Flask对象
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, flask!";


if __name__ == '__main__':
    app.run(debug=True)