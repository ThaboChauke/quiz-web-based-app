import os
from cs50 import SQL
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_mail import Mail, Message    
from helpers import login_required, json_data, history_data
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, flash, session


load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SESSION_KEY")

app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PWD")
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "sqlalchemy"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sessions.db"

sdb = SQLAlchemy(app)
app.config["SESSION_SQLALCHEMY"] = sdb
Session(app)

with app.app_context():
    sdb.create_all()

db = SQL("sqlite:///quiz.db")


@app.route("/", methods=["GET"])
@login_required
def index():
    return render_template("index.html")


@app.route("/quiz", methods=["POST", "GET"])
@login_required
def quiz():

    param = request.args.get('param')
    if not param:
        flash("No Quiz Was Chosen")
        return redirect("/")
    
    results = db.execute("SELECT * FROM quizzes WHERE topic = ?", param)

    serialized_data = json_data(results)

    return render_template("quiz.html", data=serialized_data, quiz_type=param)


@app.route("/score")
def score():

    param = request.args.get('param')
    quiz_type = request.args.get('type')

    if not param or not quiz_type:
        flash("An error ocurred", category="error")
        return redirect("/")
    
    user_id = session.get("user_id")

    try :
        results = db.execute("SELECT username FROM users WHERE id = ?", user_id)
        db.execute(
            "UPDATE users SET highscore = ? WHERE id = ? AND ? > highscore",
            param, user_id, param)
        
        db.execute(
            "UPDATE users SET overall_score = overall_score + ? WHERE id = ?",
            param, user_id)
                
        db.execute(
            "INSERT INTO history (user_id, quiz_type, score) VALUES (?, ?, ?)",
            user_id, quiz_type, param)

        result = results[0]

        if result:
            username = result["username"]

    except:
        flash("An Error Occured")
        return redirect("/")

    data = dict(username=username, user_score=param, quiz_type=quiz_type)

    return render_template("score.html", data=data)


@app.route("/history")
def history():
    user_id = session.get("user_id")

    data = db.execute("SELECT * FROM history WHERE user_id = ?", user_id)

    if data == []:
        return render_template("history.html")
    
    quzzes = history_data(data)

    return render_template("history.html", data=quzzes)


@app.route("/request", methods=["POST", "GET"])
def request_quiz():

    if request.method == "POST":
        if not request.form.get("email"):
            flash("Email is Required", category="error")
            return render_template("feedback.html")

        if not request.form.get("username"):
            flash("Username is Required", category="error")
            return render_template("feedback.html")

        if not request.form.get("quiz"):
            flash("Type is Required", category="error")
            return render_template("feedback.html")

        message = Message(
            subject="Request For Quiz",
            recipients=[os.getenv("MyEmail")],
            sender=request.form.get("email")
        )

        message.body = f"""
            {request.form.get("quiz")}

            {request.form.get("Additional")}

            from {request.form.get("username")}        
        """
        mail.send(message)

        flash("Request Sent Successfully")
        return redirect("/")

    else:
        return render_template("feedback.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":

        session.clear()

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
    return redirect("/")


@app.route("/register", methods=["POST", "GET"])
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

        if request.form.get("confirm") != request.form.get("password"):
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