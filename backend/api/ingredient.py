from . import auth
from . import db
from . import response_handler
from flask import Flask, jsonify, request, session, make_response, abort, Response


def get_all_ingredients(request):
    if auth.is_token_valid(request):
        ingredients = find_all_ingredients()
        response = make_response(jsonify(ingredients), 200)
        return response_handler.create_success_response(response)
    else:
        return response_handler.create_failure_response(403)


def find_all_ingredients():
    database = db.get_db()
    results = database.execute(
        "SELECT name FROM ingredient",
    ).fetchall()
    return create_ingredients(results)


def create_ingredients(results):
    ingredients = []
    for row in results:
        ingredients.append(row[0])
    return ingredients


