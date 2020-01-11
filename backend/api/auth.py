import uuid
from flask import Flask, jsonify, request, session, make_response
from flask_jwt_extended import create_access_token
from . import response_handler


def get_token():
    session_cookie = str(uuid.uuid4())
    access_token = create_access_token(identity=session_cookie)

    data = {'token': access_token}
    response = make_response(jsonify(data), 201)
    response.set_cookie('SESSION_ID', session_cookie)
    return response_handler.create_success_response(response)



