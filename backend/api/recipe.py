from . import db


def find_all_recipes():
    database = db.get_db()
    results = database.execute(
        "SELECT r.name, description, i.name FROM ingredient i INNER JOIN recipe r ON i.recipe_id = r.id",
    ).fetchall()

