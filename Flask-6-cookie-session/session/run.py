from flask import Flask, render_template, make_response, session

app = Flask(__name__)
app.secret_key = "test"


@app.route('/session', methods=['GET'])
def sess():
    
    resp = make_response("<html><body>Session.<a href='/getValue'>Get Value</a></body></html>")
    session['name'] = 'xugaoxiang'
    return resp


@app.route('/getValue')
def getValue():
    if 'name' in session:
        name = session['name']
        return render_template('getvalue.html', name=name)
    

if __name__ == '__main__':
    app.run(debug=True)