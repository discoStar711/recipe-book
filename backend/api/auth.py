import uuid
from datetime import datetime, timedelta
from flask import Flask, jsonify, request, session, make_response
from flask_jwt_extended import create_access_token
from . import db
from . import response_handler


def get_token():
    session_cookie = str(uuid.uuid4())
    access_token = create_access_token(identity=session_cookie)
    token_issued_time = datetime.isoformat(datetime.now())
    save_token_to_session(session_cookie, access_token, token_issued_time)

    data = {'token': access_token}
    response = make_response(jsonify(data), 201)
    response.set_cookie('SESSION_ID', session_cookie)
    return response_handler.create_success_response(response)


def save_token_to_session(session_cookie, access_token, token_issued_time):
    database = db.get_db()
    database.execute(
        "INSERT INTO userToken(session_cookie, token, issued_time) VALUES (?, ?, ?)",
        (session_cookie, access_token, token_issued_time),
    )
    database.commit()


def is_token_valid(request):
    if 'SESSION_ID' in request.cookies:
        session_cookie = request.cookies.get('SESSION_ID')
        token_to_validate = request.headers.get('token')

        return validate_token_in_session(token_to_validate, session_cookie)
    else:
        return False


def validate_token_in_session(token, session_cookie):
    current_token_in_session = find_token_by_session_id(session_cookie)
    current_datetime = datetime.now()
    token_issued_time = datetime.fromisoformat(current_token_in_session['issued_time'])
    token_timedelta = token_issued_time - current_datetime

    if token == current_token_in_session['token'] and is_token_issued_less_than_min_ago(token_timedelta):
        return True
    else:
        return False


def find_token_by_session_id(session_cookie):
    database = db.get_db()
    token = database.execute(
        "SELECT * FROM userToken WHERE session_cookie = ?",
        (session_cookie,)
    ).fetchone()
    return token


def is_token_issued_less_than_min_ago(token_timedelta):
    if token_timedelta.total_seconds() < -60.0:
        return False
    else:
        return True
