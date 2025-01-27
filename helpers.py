from functools import wraps
from flask import request, redirect,session

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def json_data(db_results):
    results = []

    for question in db_results:
        results.append({
            "id": question["id"],
            "question": question["question"],
            "option1": question["option1"],
            "option2": question["option2"],
            "option3": question["option3"],
            "option4": question["option4"],
            "correct_answer": question["correct_answer"]
        })
    return results

def history_data(data):
    result = []

    for quiz in data:
        result.append({
            "id": quiz["id"],
            "type": quiz["quiz_type"],
            "score": quiz["score"],
        })

    return result