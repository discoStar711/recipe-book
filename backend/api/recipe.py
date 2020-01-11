from . import auth
from . import db
from . import response_handler
from flask import Flask, jsonify, request, session, make_response, abort, Response


def get_all_recipes(request):
    if auth.is_token_valid(request):
        recipes = find_all_recipes()
        response = make_response(jsonify(recipes), 200)
        return response_handler.create_success_response(response)
    else:
        return response_handler.create_failure_response(403)


def find_all_recipes():
    database = db.get_db()
    results = database.execute(
        "SELECT r.name, description, i.name FROM ingredient i INNER JOIN recipe r ON i.recipe_id = r.id",
    ).fetchall()
    
