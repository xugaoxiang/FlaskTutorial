from flask import Flask

app = Flask(__name__)


@app.route('/home/<int:age>')
def index(age):
    return 'Age={}'.format(age)


if __name__ == '__main__':
    app.run(debug=True)