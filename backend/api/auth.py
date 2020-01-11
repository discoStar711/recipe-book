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



