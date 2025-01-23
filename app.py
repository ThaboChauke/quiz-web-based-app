from flask import Flask, render_template, request, redirect, flash
from cs50 import SQL
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
db = SQL("sqlite:///quiz.db")


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        pass

    else:
        return render_template("login.html")


@app.route("/register", methods = ["POST", "GET"])
def register():

    if request.method == "POST":
        
        if not request.form.get("email"):
            flash("Email is Required", category="error")
            return render_template("register.html")

        if not request.form.get("username"):
            flash("Username is Required", category="error")
            return render_template("register.html")

        if not request.form.get("password"):
            flash("Password is Required", category="error")
            return render_template("register.html")

        if not request.form.get("confirm"):
            flash("Confirm Password is Required", category="error")
            return render_template("register.html")

        if request.form.get("confirm") == request.form.get("password"):
            flash("Passwords Do Not Match", category="error")
            return render_template("register.html")

        password = generate_password_hash(request.form.get("password"))

        db.execute(
            "INSERT INTO users (username, hash, email) VALUES (?, ?, ?)", request.form.get(
            "username"), password, request.form.get("email")
        )

        flash("Registration Successful")
        return redirect("/login")
    
    else:
        return render_template("register.html")