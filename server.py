from flask import Flask, render_template, redirect, request
from user import User

app = Flask(__name__)


@app.route("/")
@app.route("/users")
def index():
    users = User.find_all()
    return render_template("index.html", users=users)

@app.route("/users/new_user")
def new_user():
    return render_template("new_user.html")

@app.post("/users/create")
def create_user():
    print(request.form)
    user_id = User.create(request.form)
    print("THIS IS THE NEW USER'S ID:" + str(user_id))
    return redirect("/users")


if __name__ == "__main__":
    app.run(debug=True)