import os
from . import db
from . import auth
from . import ingredient
from . import recipe
from flask import Flask, jsonify, request, session, make_response
from flask_jwt_extended import JWTManager
from flask_cors import CORS


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'api.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.config['JWT_SECRET_KEY'] = '1234'
    JWTManager(app)
    CORS(app, supports_credentials=True)

    return app
