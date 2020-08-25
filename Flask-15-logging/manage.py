from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    app.logger.debug(f'login success.')
    return jsonify(
        {
            "code": 200
        }
    )
        
if __name__ == '__main__':
    app.run(debug=True, port=5000)