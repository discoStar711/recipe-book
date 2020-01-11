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
    return create_recipes(results)


def create_recipes(results):
    recipes = []
    current_recipes = []

    for row in results:
        name_key = 'name'
        name_value = row[0]
        description_key = 'description'
        description_value = row[1]
        ingredient_key = 'ingredients'
        ingredient_value = row[2]

        if len(recipes) == 0:
            recipes.append(create_recipe(name_key, name_value, description_key, description_value, ingredient_key,
                                         ingredient_value))
            current_recipes.append(name_value)
        else:
            for result in recipes:
                if result[name_key] == name_value:
                    if not is_ingredient_exist(result[ingredient_key], ingredient_value):
                        result[ingredient_key].append(ingredient_value)

                if is_recipe_exist(current_recipes, name_value):
                    continue

                recipes.append(create_recipe(name_key, name_value, description_key, description_value, ingredient_key,
                                             ingredient_value))
                current_recipes.append(name_value)

    return recipes


def is_recipe_exist(current_recipes, name):
    return is_exist(current_recipes, name)


def is_ingredient_exist(current_ingredients, name):
    return is_exist(current_ingredients, name)


def is_exist(list, name):
    for item in list:
        if item == name:
            return True
    return False


def create_recipe(name_key, name_value, description_key, description_value, ingredient_key, ingredient_value):
    new_recipe = {}
    new_recipe[name_key] = name_value
    new_recipe[description_key] = description_value
    new_recipe[ingredient_key] = []
    new_recipe[ingredient_key].append(ingredient_value)
    return new_recipe
