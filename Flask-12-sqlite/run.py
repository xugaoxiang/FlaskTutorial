from flask import *
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/savedetails", methods=["POST", "GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            with sqlite3.connect("users.db") as con:
                cur = con.cursor()
                cur.execute("insert into user (name, email) values (?,?)", (name, email))
                con.commit()
                msg = "user successfully added"
        except:
            con.rollback()
            msg = "We can't add the employee to the list"
        finally:
            return render_template("success.html", msg=msg)
            con.close()


@app.route("/view")
def view():
    con = sqlite3.connect("users.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from user")
    rows = cur.fetchall()
    return render_template("view.html", rows=rows)


@app.route("/delete")
def delete():
    return render_template("delete.html")


@app.route("/delete_user", methods=["POST"])
def deleterecord():
    id = request.form["id"]
    with sqlite3.connect("users.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from user where id = ?", id)
            msg = "record successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return render_template("delete_user.html", msg=msg)


if __name__ == "__main__":
    app.run(debug=True)