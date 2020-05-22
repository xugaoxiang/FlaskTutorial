from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "xxx"


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        if request.form['email'] != 'test@gmail.com' or request.form['password'] != 'test':
            error = "Invalid account."
        else:
            flash("Login successfully")
            return redirect(url_for('index'))
    
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)