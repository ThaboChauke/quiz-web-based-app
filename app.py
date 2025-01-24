from flask import Flask, render_template, request, redirect, flash, session
from cs50 import SQL
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from flask_session import Session
from redis import StrictRedis
import os


load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SESSION_KEY")

HOST = os.getenv("REDIS_HOST")
PORT = os.getenv("REDIS_PORT")
PASSWORD  = os.getenv("REDIS_PASSWORD")

app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_REDIS'] = StrictRedis(host=HOST, port=PORT, password=PASSWORD, decode_responses=True)
Session(app)

db = SQL("sqlite:///quiz.db")


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":

        if not request.form.get("username"):
            flash("Username is Required", category="error")
            return render_template("login.html")

        if not request.form.get("password"):
            flash("Password is Required", category="error")
            return render_template("login.html")
        
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            flash("Incorrect Password or Username", category="error")
            return render_template("login.html")
        
        
        session["user_id"] = rows[0]["id"]

        flash("Log in Successful")
        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():

    session.clear()
    flash("You have been logged out")
    redirect("/")


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