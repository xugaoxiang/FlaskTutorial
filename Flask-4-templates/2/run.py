from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<name>')
def index(name):
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)