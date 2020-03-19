from flask import Flask, make_response

app = Flask(__name__)


@app.route('/cookie', methods=['GET'])
def cookie():
    
    resp = make_response("<html><body>Cookie</body></html>")
    resp.set_cookie('name', 'xugaoxiang')
    return resp


if __name__ == '__main__':
    app.run(debug=True)