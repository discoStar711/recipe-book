from flask import jsonify, make_response, Response


def create_success_response(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    response.headers["Access-Control-Allow-Credentials"] = 'true'
    return response


def create_failure_response(http_status):
    response = make_response(jsonify({'error': 'Something went wrong'}), http_status)
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    response.headers["Access-Control-Allow-Credentials"] = 'true'
    return response