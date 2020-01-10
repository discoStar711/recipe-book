DROP TABLE IF EXISTS recipe;
DROP TABLE IF EXISTS ingredient;
DROP TABLE IF EXISTS userToken;

CREATE TABLE recipe(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
);

CREATE TABLE ingredient(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    recipe_id INTEGER NOT NULL,
    FOREIGN KEY (recipe_id) REFERENCES recipe (id)
);

CREATE TABLE userToken(
    session_cookie TEXT NOT NULL,
    token TEXT NOT NULL,
    issued_time TEXT NOT NULL
);

INSERT INTO recipe(name, description) VALUES
    ('Recipe 1', 'Description 1'),
    ('Recipe 2', 'Description 2'),
    ('Recipe 3', 'Description 3'),
    ('Recipe 4', 'Description 4');

INSERT INTO ingredient(name, recipe_id) VALUES
    ('Ingredient 1', 1),
    ('Ingredient 2', 1),
    ('Ingredient 3', 2),
    ('Ingredient 4', 2),
    ('Ingredient 5', 3),
    ('Ingredient 6', 3),
    ('Ingredient 7', 4),
    ('Ingredient 8', 4);

