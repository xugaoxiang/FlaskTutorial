from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/validate', methods=['POST'])
def validate():
    if request.method == 'POST' and request.form['email'] == 'test@gmail.com' and request.form['password'] == 'test':
        return redirect(url_for('success'))
    
    return redirect(url_for('login'))
    

@app.route('/success')
def success():
    return 'Logged in successfully.'


if __name__ == '__main__':
    app.run(debug=True)